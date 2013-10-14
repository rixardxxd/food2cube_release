from django.http import HttpResponse, HttpResponseServerError

from django.shortcuts import render,get_object_or_404

from django.contrib.auth import authenticate,login,logout

from mainSite.models import MyUser

import json


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

    email = request.POST['email']
    password = request.POST['password']
    first_name = request.POST['first_name']
  #  middle_name = request.POST['middle_name']
    last_name = request.POST['last_name']
    phone_number = request.POST['phone_number']
  #  street = request.POST['street']
  # city = request.POST['city']
  #  state = request.POST['state']
  #  zip_code = request.POST['zip_code']
    company = request.POST['company']

    user = MyUser.objects.create_user(email=email,first_name=first_name,last_name=last_name,phone_number=phone_number,
                                      company=company,password=password)
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



