from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_micro_focus_admin, name="micro_focus_admin_login"),
    path(
        "dashboard/",
        views.micro_focus_admin_dashboard,
        name="micro_focus_admin_dashboard",
    ),
    path("revoke_key/", views.revoke_key, name="revoke_key"),
    path("add_access_key/", views.add_access_key, name="add_access_key"),
    path("dashboard/", views.micro_focus_admin_dashboard, name="dashboard"),
]
