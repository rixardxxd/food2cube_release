from django.http import HttpResponse

from django.shortcuts import render,get_object_or_404

from django.contrib.auth import authenticate,login,logout


def login_user(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)


    if user is not None:
    # the password verified for the user
        if user.is_active:
            login(request,user)
            print("User is valid, active and authenticated")
            return HttpResponse("100")
        else:
            print("The password is valid, but the account has been disabled!")
            return HttpResponse("101")
    else:
    # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")
        return HttpResponse("102")


def logout_user(request):

    logout(request)
    print("The user has been logged out.")
    return HttpResponse("99")



