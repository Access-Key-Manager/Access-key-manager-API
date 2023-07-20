from django.shortcuts import render, redirect
from authentication.forms import SchoolSignUpForm, SignUpForm
from users.models import SchoolITPersonnel

# Create your views here.
# todo: Move all things related to authentication and the users
# this has to do with admins, it personnels and any actor who is
# a user to the 'users' model'


def user_sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()

            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "authentication/user_signup.html", {"form": form})


def school_sign_up(request):
    if request.method == "POST":
        form = SchoolSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SchoolSignUpForm()
    return render(request, "authentication/school_sign_up.html", {"form": form})
