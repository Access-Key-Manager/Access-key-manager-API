from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from school.models import School, SchoolITPersonnel
from django.utils.translation import gettext_lazy as _


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    school = forms.ModelChoiceField(queryset=School.objects.all())

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["username"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def clean_password1(self):
        data = self.cleaned_data["password1"]

        if len(data) < 8:
            raise ValidationError(
                _("Your password must contain at least 8 characters.")
            )

        if data.isnumeric():
            raise ValidationError(_("Your password can’t be entirely numeric."))

        return data

    def clean_password2(self):
        pass1 = self.cleaned_data.get("password1")
        pass2 = self.cleaned_data.get("password2")

        if pass1 != pass2 and pass1 and pass2:
            raise ValidationError(_("Your passwords do not match"))

        return pass2


class SchoolSignUpForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ["name", "email", "school_type"]
