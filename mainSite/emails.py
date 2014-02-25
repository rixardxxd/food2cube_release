__author__ = 'fangyuew'

"""
Utility Functions
"""
import logging
log = logging.getLogger(__name__)
import json
from django.core.mail import EmailMultiAlternatives
import sendgrid
from models import MyUser, Transaction, Order, OrderLine

fromEmail =  'xingxiaodi@yahoo.com'
subject_template='-name-, Thank you for ordering in food2cube!'
content_text_template="""\
    Dear -name-,
    We have received your order with following details:
    -order_detail-
    and we have received your payment of $-total-

    The order will be delivered to you soon,
    Have good meal!

    Regards,
    food2cube
    """

content_html_template="""\
    <html>
        <head></head>
        <body>
        <>
        <p>Hi! -name-<br>
           Thanks for ordering in food2cube!<br>
           Food ordered is:<br>
           -order_detail_html- <br>
           and we have received your payment of $-total- <br>

           The food will delivered to you soon, enjoy! <br>
           <br>
           Regards,<br>
           food2cube
        </p>

        </body>
    </html>
    """

def sendOrderEmailToRestaurants():

    rest_order=[]








    return;

def sendDeliverEmailToRestaurants():

    rest_order=[]








    return;



def sendConfirmEmailOld(user_id, transaction_id, order_id):

    log.info("Sending Confirm Email")

    #prepare objects
    myuser = MyUser.objects.get(id=user_id)
    transaction = Transaction.objects.get(id=transaction_id)

    #prepare email
    hdr = SmtpApiHeader()

    receiver = [myuser.email]
    names = [myuser.get_name()]
    totals = [float(transaction.total_amount)]

    order = Order.objects.get(id=order_id)
    order_detail=''
    order_detail_html=''

    orderlines=OrderLine.objects.filter(order=order)
    for orderline in orderlines:
        order_detail+=str(orderline)+"\n"
        order_detail_html+=str(orderline)+"<br>"

    log.info("Order Detail:")
    log.info(order_detail)
    log.info(order_detail_html)

    hdr.addTo(receiver)
    hdr.addSubVal('-total-', totals)
    hdr.addSubVal('-name-', names)
    hdr.addSubVal('-order_detail-', [order_detail])
    hdr.addSubVal('-order_detail_html-', [order_detail_html])

    hdr.setCategory("initial")  # Specify that this is an initial contact message
    hdr.addFilterSetting('footer', 'enable', 1)
    hdr.addFilterSetting('footer', "text/plain", "Thank you for your business!")

    msg = EmailMultiAlternatives(subject_template, content_text_template, fromEmail, receiver, headers={"X-SMTPAPI": hdr.asJSON()})
    msg.attach_alternative(content_html_template, "text/html")
    msg.send()

    return



def sendConfirmEmail(ipn_obj):

    if ipn_obj.custom is not None:
        log.info(ipn_obj.custom)
        strings = ipn_obj.custom.split("|")

    if len(strings) >=3:
        name = strings[0]
        email = strings[1]
        phone = strings[2]
    log.info("Sending Confirm Email to" + name + " " + email + " " + phone)

    #prepare objects
    #myuser = MyUser.objects.get(id=user_id)
    #transaction = Transaction.objects.get(id=transaction_id)

    #prepare email
    hdr = SmtpApiHeader()

    receiver = [email]
    names = name
    totals = 0

    log.info("mc gross ", ipn_obj.mc_gross)
    log.info("cart item number ", ipn_obj.num_cart_items)
    log.info("item 1 name ",ipn_obj.item_name1)
    log.info("item 1 amount ",ipn_obj.quantity1)
    log.info("item 2 name ",ipn_obj.item_name2)
    log.info("item 2 amount ",ipn_obj.quantity2)
   
    order_detail='here is the detail'
    order_detail_html='here is the detail html'

 

    log.info("Order Detail:")
    log.info(order_detail)
    log.info(order_detail_html)

    hdr.addTo(receiver)
    hdr.addSubVal('-total-', [totals])
    hdr.addSubVal('-name-', [names])
    hdr.addSubVal('-order_detail-', [order_detail])
    hdr.addSubVal('-order_detail_html-', [order_detail_html])

    hdr.setCategory("initial")  # Specify that this is an initial contact message
    hdr.addFilterSetting('footer', 'enable', 1)
    hdr.addFilterSetting('footer', "text/plain", "Thank you for your business!")

    msg = EmailMultiAlternatives(subject_template, content_text_template, fromEmail, receiver, headers={"X-SMTPAPI": hdr.asJSON()})
    msg.attach_alternative(content_html_template, "text/html")
    msg.send()

    return

import re
import textwrap

class SmtpApiHeader:

    def __init__(self):
        self.data = {}

    def addTo(self, to):
        if not self.data.has_key('to'):
            self.data['to'] = []
        if type(to) is str:
            self.data['to'] += [to]
        else:
            self.data['to'] += to

    def addSubVal(self, var, val):
        if not self.data.has_key('sub'):
            self.data['sub'] = {}
        if type(val) is str:
            self.data['sub'][var] = [val]
        else:
            self.data['sub'][var] = val

    def setUniqueArgs(self, val):
        if type(val) is dict:
            self.data['unique_args'] = val

    def setCategory(self, cat):

        self.data['category'] = cat

    def addFilterSetting(self, fltr, setting, val):
        if not self.data.has_key('filters'):
            self.data['filters'] = {}
        if not self.data['filters'].has_key(fltr):
            self.data['filters'][fltr] = {}
        if not self.data['filters'][fltr].has_key('settings'):
                self.data['filters'][fltr]['settings'] = {}
        self.data['filters'][fltr]['settings'][setting] = val

    def asJSON(self):
        j = json.dumps(self.data)
        return re.compile('(["\]}])([,:])(["\[{])').sub('\1\2 \3', j)

    def as_string(self):
        j = self.asJSON()
        str = 'X-SMTPAPI: %s' % textwrap.fill(j, subsequent_indent = '  ', width = 72)
        return str

"""
hdr = SmtpApiHeader.SmtpApiHeader()
    # The list of addresses this message will be sent to
    receiver = ['isaac@example.com', 'tim@example.com', 'jose@example.com']

    # The names of the recipients
    times = ['1pm', '2pm', '3pm']

    # Another subsitution variable
    names = ['Isaac', 'Tim', 'Jose']

    # Set all of the above variables
    hdr.addTo(receiver)
    hdr.addSubVal('-time-', times)
    hdr.addSubVal('-name-', names)

    # Specify that this is an initial contact message
    hdr.setCategory("initial")

    # Enable a text footer and set it
    hdr.addFilterSetting('footer', 'enable', 1)
    hdr.addFilterSetting('footer', "text/plain", "Thank you for your business!")

    # fromEmail is your email
    # toEmail is recipient's email address
    # For multiple recipient e-mails, the 'toEmail' address is irrelivant
    fromEmail =  'testing@sendgrid.net'
    toEmail = 'sendgrid@hotmail.com'

    # Create message container - the correct MIME type is multipart/alternative.
    # Using Django's 'EmailMultiAlternatives' class in this case to create and send.
    # Create the body of the message (a plain-text and an HTML version).
    # text is your plain-text email
    # html is your html version of the email
    # if the reciever is able to view html emails then only the html
    # email will be displayed
    subject = 'Contact Response for <-name-> at <-time->'
    text_content = 'Hi -name-!\nHow are you?\n'
    html =
    <html>
        <head></head>
        <body>
        <p>Hi! -name-<br>
           How are you?<br>
        </p>
        </body>
    </html>
    """
#    msg = EmailMultiAlternatives(subject, text_content, fromEmail, [toEmail], headers={"X-SMTPAPI": hdr.asJSON()})
#    msg.attach_alternative(html, "text/html")
#    msg.send()

