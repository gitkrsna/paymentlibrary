from django.conf.urls import url
from django.views.generic import TemplateView
from .views import *




urlpatterns = [
    url(r'^checkout/$', checkout_page, name="checkout"),
    url(r'^payment/$', payment, name="payment"),
]