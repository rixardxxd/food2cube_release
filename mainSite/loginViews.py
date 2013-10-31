from django.http import HttpResponse, HttpResponseServerError

from django.shortcuts import render,get_object_or_404

from django.contrib.auth import authenticate,login,logout

from mainSite.models import MyUser

from django.db import IntegrityError

import json

import logging
log = logging.getLogger(__name__)

def login_user(request):

    json_data = json.loads(request.raw_post_data)
    email = ''
    password = ''
    try:
        email = json_data['email']
        password = json_data['password']
    except KeyError:
        HttpResponseServerError("Malformed data!")


    user = authenticate(username=email, password=password)


    if user is not None:
    # the password verified for the user
        if user.is_active:
            login(request,user)
            print("User is valid, active and authenticated")

            return HttpResponse()
        else:
            print("The password is valid, but the account has been disabled!")
            res = HttpResponse()
            res.status_code = 401
            return res
    else:
    # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")
        res = HttpResponse()
        res.status_code = 401
        return res


def signup_user(request):

    json_data = json.loads(request.raw_post_data)
    email = ''
    password = ''
    firstname = ''
    lastname = ''
    phone = ''
    try:
        email = json_data['email']
        password1 = json_data['password1']
        password2 = json_data['password2']
        firstname = json_data['firstname']
        lastname = json_data['lastname']
        phone = json_data['phone']
    except KeyError:
        return HttpResponseServerError("Malformed data!")
    if password1 != password2:
        return HttpResponseServerError("Two passwords does not match!")

    log.info(email + '')
    log.info(password1 + '')
    log.info(firstname + '')
    log.info(lastname + '')
    log.info(phone  + '')

    try:
        user = MyUser.objects.create_user(email=email,first_name=firstname,last_name=lastname,phone_number=phone,
                                      password=password2)
    except IntegrityError as e:
        return HttpResponseServerError(e.message)
    except Exception as e:
        return HttpResponseServerError(e.message)


    if user is not None:
        return HttpResponse()
    else:
        res = HttpResponse()
        res.status_code = 401
        return res



def logout_user(request):

    logout(request)
    print("The user has been logged out.")
    return HttpResponse()



