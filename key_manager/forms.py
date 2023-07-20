import datetime
from key_manager.models import AccessKey
from django import forms
from django.core.exceptions import ValidationError

from school.models import School


# class AddAccessKeyForm(forms.ModelForm):
#     class Meta:
#         model = AccessKey
#         exp_date = forms.DateField()

#         fields = ["expiry_date"]

#         def clean_expiry_date(self):
#             data = self.cleaned_data["exp_date"]

#             if data < datetime.date.today():
#                 raise forms.ValidationError(_("Invalid date - expiry date in the past"))
#             return data < datetime.date.today() + datetime.timedelta(4)
