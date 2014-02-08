from paypal.standard.ipn.signals import payment_was_successful
import logging
def save_payment_and_send_email(sender, **kwargs):
    ipn_obj = sender

    log = logging.getLogger('mainSite')
    log.info('aaaaaaaaa')
    log.info(sender)
    print __file__,1, 'This works'
    if ipn_obj.custom is not None:
        log.info(ipn_obj.custom)



#Here is the payment successful signal passed from the django paypal
payment_was_successful.connect(save_payment_and_send_email)
