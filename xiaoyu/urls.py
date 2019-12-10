from django.urls import path
from . import views

app_name = "xiaoyu"

urlpatterns = [
    path('index/',views.index,name="index")
]