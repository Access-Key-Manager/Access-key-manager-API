from django.shortcuts import redirect, render

# Create your views here.

from django.shortcuts import render, get_object_or_404

from key_manager.models import AccessKey
from rest_framework.views import APIView
from django.views import generic
from django.views.generic import ListView, DetailView

from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import permissions

# Create your views here.


class AccessKeysListView(ListView):
    model = AccessKey
    paginate_by = 10
    template_name = "school/access_key_list.html"
    context_object_name = "access_key_list"


# def all_access_keys(request, id_of_school):
#     school = get_object_or_404(School, pk=id_of_school)

#     return render(request, "accesskeys.html", context={"keys": school.all_access_keys})


class AccessKeysDetailView(DetailView):
    model = AccessKey
    template_name = "access_key_detail.html"
    context_object_name = "access_key_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accesskey_list"] = AccessKey.object.all()
        return context


class FilterAccessKeys(generic.ListView):
    model = AccessKey
    paginate_by = 10

    def get_queryset(self):
        context_object_name = "filter_list"
        return AccessKey.objects.filter(status=self.kwargs["status"])


# class FilterAccessKeys(APIView):
#     permission_classes=[permissions.IsAuthenticatedOrReadOnly]
#     def post (self,request,*args,**kwargs):
#         access_key_status= request.data.get('access_key_status')

#         key_status=AccessKey.objects.filter(access_key_status=access_key_status)
