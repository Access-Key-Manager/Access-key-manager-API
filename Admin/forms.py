from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MicroFocusAdmin, AccessKey
from django.shortcuts import render, redirect

# from Admin.forms import AddAccessKeyForm


class Form(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MicroFocusAdmin
        fields = ["email"]


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class AddAccessKeyForm(forms.Form):
    key_name = forms.CharField(max_length=100)
    date_of_procurement = forms.DateField()
    expiry_date = forms.DateField()


def add_access_key(request):
    if request.method == "POST":
        form = AddAccessKeyForm(request.POST)
        if form.is_valid():
            key_name = form.cleaned_data["key_name"]
            date_of_procurement = form.cleaned_data["date_of_procurement"]
            expiry_date = form.cleaned_data["expiry_date"]

            # Save the new access key to the database
            AccessKey.objects.create(
                key_name=key_name,
                date_of_procurement=date_of_procurement,
                expiry_date=expiry_date,
            )
            return redirect(
                "access_keys_list"
            )  # Redirect to the list of access keys after adding the new key
    else:
        form = AddAccessKeyForm()
    return render(request, "add_access_key.html", {"form": form})
