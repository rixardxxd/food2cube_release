__author__ = 'fangyuew'

"""
Utility Functions
"""
import logging
log = logging.getLogger(__name__)
import sendgrid

def sendEmail( email , message ):


    return False;

def sendEmails( emailList , message ):
    success = True
    for email in emailList:
        tmp = sendEmail(email, message)
        if tmp is False:
            log.error("Failed to send email to ["+email+"] with content ["+message+"]")
        success &= tmp
    return success;