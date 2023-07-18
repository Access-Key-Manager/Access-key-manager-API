from authentication import views
from django.urls import path

urlpatterns = [
    path("user_signup/", views.user_sign_up, name="user_sign-up"),
    path("school_signup/", views.school_sign_up, name="school-sign-up"),
]
