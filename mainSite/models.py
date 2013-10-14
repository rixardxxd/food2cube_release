from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class MyUserManager(BaseUserManager):
    def create_user(self, email,first_name,last_name,phone_number,company,
                        password,middle_name="",street="", city="",state="",zip_code=0,):

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


    def create_superuser(self, email,first_name,last_name,phone_number,company,
                        password,middle_name="",street="", city="",state="",zip_code=0,):

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
    company = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','first_name','last_name','company',]

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

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Company(models.Model):
    name=models.CharField(max_length=100)
    street = models.CharField(max_length=100,blank=True,default="",)
    city = models.CharField(max_length=100,blank=True,default="",)
    state = models.CharField(max_length=100,blank=True,default="",)
    zip_code = models.IntegerField(blank=True,default=0,)

    def __unicode__(self):
       return  self.name





class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    street = models.CharField(max_length=100,blank=True,default="",)
    city = models.CharField(max_length=100,blank=True,default="",)
    state = models.CharField(max_length=100,blank=True,default="",)
    zip_code = models.IntegerField(blank=True,default=0,)
    nearby_company = models.ManyToManyField(Company)

    def __unicode__(self):
        return  self.name



class Menu(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=300,blank=True,default="",)
    category = models.CharField(max_length=100,blank=True,default="",)
    restaurant = models.ForeignKey(Restaurant,related_name="menus")

    def __unicode__(self):
        return self.name






