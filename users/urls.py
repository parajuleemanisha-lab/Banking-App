from .views import account_opening
from django.urls import path

urlpatterns = [
    path('',account_opening,name='home')
]