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
