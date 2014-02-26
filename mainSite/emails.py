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
        <img src ='/static/mainSite/app/img/Food2Cube_Font_Final.png' width='150' height='75'>
        <p>Hi! -name-<br>
           Thanks for ordering in food2cube!<br>
           Food ordered is:<br>
           -item_name1-  -quantity1- <br>
           -item_name2-  -quantity2- <br>
           and we have received your payment of $-total- <br>
           We will contact you by phone number -phone-<br>
           The food will be delivered to: <br>
           <br>
           Cisco parking lot A @12:30 pm <br>
           <br>
           If any of the above information is not correct, <br>
           please reply to this email as soon as possible!<br>
           <br>
           Best regards,<br>
           food2cube
        </p>

        <img>
        </body>
    </html>
    """




def sendConfirmEmail(ipn_obj):

    if ipn_obj.custom is not None:
        log.info(ipn_obj.custom)
        strings = ipn_obj.custom.split("|")

    if len(strings) >=3:
        name = strings[0]
        phone = strings[1]
        email = strings[2]
    log.info("Sending Confirm Email to " + name + " " + email + " " + phone)

    #prepare objects
    #myuser = MyUser.objects.get(id=user_id)
    #transaction = Transaction.objects.get(id=transaction_id)

    #prepare email
    hdr = SmtpApiHeader()

    receiver = email
    names = name
    totals = str(ipn_obj.mc_gross)

    item_name1 = find_between(ipn_obj.query,"item_name1=","&")
    item_name2 = find_between(ipn_obj.query,"item_name2=","&")
    quantity1 = find_between(ipn_obj.query,"quantity1=","&")
    quantity2 = find_between(ipn_obj.query,"quantity2=","&")



    log.info("mc gross %f" % ipn_obj.mc_gross)
    log.info("query " + ipn_obj.query)
    log.info("cart item number %d" % ipn_obj.num_cart_items)
    log.info("item_name1 %s" % item_name1)
    log.info("item_name2 %s" % item_name2)
    log.info("quantity1 %s" % quantity1)
    log.info("quantity2 %s" % quantity2)



    hdr.addTo([receiver])
    hdr.addSubVal('-total-', [totals])
    hdr.addSubVal('-name-', [names])
    hdr.addSubVal('-phone-', [phone])
    hdr.addSubVal('-item_name1-', [item_name1])
    hdr.addSubVal('-item_name2-', [item_name2])
    hdr.addSubVal('-quantity1-', [quantity1])
    hdr.addSubVal('-quantity2-', [quantity2])

    hdr.setCategory("initial")  # Specify that this is an initial contact message
    hdr.addFilterSetting('footer', 'enable', 1)
    hdr.addFilterSetting('footer', "text/plain", "Thank you for your business!")

    msg = EmailMultiAlternatives(subject_template, content_html_template, fromEmail, receiver, headers={"X-SMTPAPI": hdr.asJSON()})
    msg.attach_alternative(content_html_template, "text/html")
    msg.send()

    return

import re
import textwrap

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


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


