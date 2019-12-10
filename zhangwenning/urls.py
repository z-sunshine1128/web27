from django.urls import path
from . import views

app_name = "zhangwenning"

urlpatterns = [
    path('index/',views.index,name="index")
]