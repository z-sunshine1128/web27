from django.urls import path
from . import views

app_name = "zhaoyao"

urlpatterns = [
    path('index/',views.index,name="index")
]