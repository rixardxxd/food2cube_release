from paypal.standard.ipn.signals import payment_was_successful
import logging
def save_payment_and_send_email(sender, **kwargs):
    ipn_obj = sender
    log = logging.getLogger(__name__)
    log.info('aaaaaaaaa')
    log.info(sender)

payment_was_successful.connect(save_payment_and_send_email)
