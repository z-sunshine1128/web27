from django.contrib import admin
from django.urls import path
from . import views

app_name = "yanminqi"

urlpatterns = [
    path('index/',views.index,name="index")
]
