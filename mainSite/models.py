from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

#This is the model class

class MyUserManager(BaseUserManager):
    def create_user(self, email,first_name,last_name,phone_number,
                        password,company="",middle_name="",street="", city="",state="",zip_code=0,):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            phone_number = phone_number,
            street = street,
            city = city,
            state = state,
            zip_code = zip_code,
            company = company,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email,first_name,last_name,phone_number,
                        password,company="",middle_name="",street="", city="",state="",zip_code=0,):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            phone_number = phone_number,
            street = street,
            city = city,
            state = state,
            zip_code = zip_code,
            company = company,
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    email = models.EmailField(
       verbose_name='email address',
      max_length=255,
       unique=True,
       db_index=True,
    )
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,blank=True,default="",)
    last_name = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    street = models.CharField(max_length=100,blank=True,default="",)
    city = models.CharField(max_length=100,blank=True,default="",)
    state = models.CharField(max_length=100,blank=True,default="",)
    zip_code = models.IntegerField(blank=True,default=0,)
    company = models.CharField(max_length=100,blank=True,default="",)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','first_name','last_name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_name(self):
        return self.first_name + " " + self.last_name

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Company(models.Model):
    name=models.CharField(max_length=100)
    group_name=models.CharField(max_length=100,blank=True)
    street = models.CharField(max_length=100,blank=True,default="",)
    city = models.CharField(max_length=100,blank=True,default="",)
    state = models.CharField(max_length=100,blank=True,default="",)
    zip_code = models.IntegerField(blank=True,default=0,)

    def __unicode__(self):
        return  self.name

    def getAddress(self):
        return "{0}, {1}, {2} {3}".format(self.street,self.city,self.state,self.zip_code)


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,db_index=True)
    street = models.CharField(max_length=100,blank=True,default="",)
    city = models.CharField(max_length=100,blank=True,default="",)
    state = models.CharField(max_length=100,blank=True,default="",)
    zip_code = models.IntegerField(blank=True,default=0,)
    nearby_company = models.ManyToManyField(Company)

    def __unicode__(self):
        return  self.name

    def getAddress(self):
        return "{0}, {1}, {2} {3}".format(self.street,self.city,self.state,self.zip_code)


class Menu(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=300,blank=True,default="",)
    category = models.CharField(max_length=100,blank=True,default="",)
    restaurant = models.ForeignKey(Restaurant,related_name="menus")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.name


#Following is data models defined for order and transaction system
#Terms:
#       Order : A placement that may contain a combination of different dishes of various quantity
#       OrderLine : A line of an order, containing a certain dish and it's quantity
#       Transaction : One financial transaction report recording key information of a transaction
class Order(models.Model):
    user = models.ForeignKey(MyUser)
    dest_company = models.ForeignKey(Company)
    deliver_address = models.CharField(max_length=1024, blank=True, default="")
    message = models.CharField(max_length=1024, blank=True, default="")
    restaurants = models.ManyToManyField(Restaurant)
    order_lines_string = models.CharField(max_length=4096,blank=True,default="")
    order_time = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    delivered = models.BooleanField(default = False)

    def __unicode__(self):
        return self.user.email + " " + self.dest_company.name + " " + str(self.order_time)


class OrderLine(models.Model):
    order = models.ForeignKey(Order)
    menu = models.ForeignKey(Menu)
    quantity = models.IntegerField(default=1)

    def __unicode__(self):
        return self.menu.name + " * " + str(self.quantity)


class Transaction(models.Model):
    user = models.ForeignKey(MyUser)
    dest_company = models.ForeignKey(Company)
    restaurants = models.ManyToManyField(Restaurant)
    company_name = models.CharField(max_length=100)
    restaurant_names = models.CharField(max_length=1048)
    transaction_time = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return self.user.email + " " + str(self.total_amount)


from paypal.standard.ipn.signals import payment_was_successful,payment_was_flagged
import logging
log = logging.getLogger(__name__)


def save_payment_and_send_email(sender, **kwargs):
    ipn_obj = sender
    log.info('aaaaaaaaa')
    log.info(sender)
    print __file__,1, 'This works'
    if ipn_obj.custom is not None:
        log.info(ipn_obj.custom)



def payment_flagged(sender, **kwargs):
    log.info("FLAGGED: %s" % sender.payer_email)

#Here is the payment successful signal passed from the django paypal
payment_was_successful.connect(save_payment_and_send_email)
payment_was_flagged.connect(payment_flagged)