from school.views import AccessKeysListView, AccessKeysDetailView
from school import views
from django.urls import path

urlpatterns = [
    path("access_keys/", AccessKeysListView.as_view(), name="access-key-list"),
    path(
        "access_keys/<int:id>",
        AccessKeysDetailView.as_view(),
        name="access-key-detail",
    ),
]
