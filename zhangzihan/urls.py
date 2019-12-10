from django.urls import path
from . import views

app_name = "zhangzihan"

urlpatterns = [
    path('index/',views.index,name="index")
]