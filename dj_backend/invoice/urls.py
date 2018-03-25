from django.urls import path,re_path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('invoice/', views.InvoiceList.as_view()),
    re_path(r'^invoice/(?P<pk>[0-9]+)/$', views.InvoiceDetail.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
