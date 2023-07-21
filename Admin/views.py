import datetime
from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from key_manager.models import AccessKey
from school.models import School
from .forms import Form, LoginForm


def register_micro_focus_admin(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "login"
            )  # Redirect to the login page after successful registration
    else:
        form = Form()
    return render(request, "register_micro_focus_admin.html", {"form": form})


def login_micro_focus_admin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(
                    "dashboard"
                )  # Redirect to the Micro-Focus Admin dashboard
    else:
        form = LoginForm()
    return render(request, "login_micro_focus_admin.html", {"form": form})


def micro_focus_admin_dashboard(request):
    return render(request, "dashboard.html", context)


def revoke_key(request, id):
    context = {}
    acc_key = get_object_or_404(AccessKey, id=id)
    if request.method == "GET":
        acc_key.status = AccessKey.AccessKeyStatus.REVOKED
        return redirect("")
    return render(request, "admin/revoke_accesskey.html", context)


def add_access_key(request):
    school = get_object_or_404(School, request.self.id == id)

    accesskey = AccessKey.objects.create(school=school)
    if school.payment_plan == School.PaymentPlanStatus.MONTHLY:
        accesskey.expiry_date = datetime.date.today() + datetime.timedelta(4)
    elif school.payment_plan == School.PaymentPlanStatus.QUARTERLY:
        accesskey.expiry_date = datetime.date.today() + datetime.timedelta(17)
    elif school.payment_plan == School.PaymentPlanStatus.YEARLY:
        accesskey.expiry_date = datetime.date.today() + datetime.timedelta(52)
    AccessKey.status = AccessKey.AccessKeyStatus.ACTIVATED

    AccessKey.save()
