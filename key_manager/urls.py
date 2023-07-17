from django.urls import path
from key_manager import views

urlpatterns = [
    path("purchase_access_key/", views.purchase_accesskey, name="add-access-key"),
    path("revoke_access_key/", views.revoke_accesskey, name="revoke-access-key"),
    path("home/", views.index, name="index"),
]
