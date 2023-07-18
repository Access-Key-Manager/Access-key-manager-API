import datetime
from django.shortcuts import render, get_object_or_404, redirect

from key_manager.models import AccessKey
from rest_framework.views import APIView
from django.views import generic
from django.views.generic import ListView

from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import permissions

from django.forms import ModelForm

# from key_manager.forms import AddAccessKeyForm
from school.models import School

# Create your views here.


def index(request):
    return render(request, "index.html")


# @login_required
# @permission_required
# def add_accesskey(request):
#     if request.method == "POST":
#         form = AddAccessKeyForm(request.POST)

#         if form.is_valid():

#             AccessKey.expiry_date = form.cleaned_data["exp_date"]
#             AccessKey.status = AccessKey.AccessKeyStatus.ACTIVATED
#             form.save()
#             return redirect("index")
#     else:
#         form = AddAccessKeyForm()
#     return render(request, "admin/add_accesskey.html", {"form": form})


def purchase_accesskey(request):
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


# def edit_access_key(request):
#     if request.method=='GET':
def expire_accesskey(request, id):
    context = {}
    acc_key = get_object_or_404(AccessKey, id=id)
    if request.method == "GET":
        acc_key.status = AccessKey.AccessKeyStatus.REVOKED
        return redirect("")
    return render(request, "admin/revoke_accesskey.html", context)


# @login_required
# @permission_required
def revoke_accesskey(request, id):
    context = {}
    acc_key = get_object_or_404(AccessKey, id=id)
    if request.method == "GET":
        acc_key.status = AccessKey.AccessKeyStatus.REVOKED
        return redirect("")
    return render(request, "admin/revoke_accesskey.html", context)
