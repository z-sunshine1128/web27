from django.urls import path
from . import views

app_name = "dutailong"

urlpatterns = [
    path('index/',views.index,name="index")
]