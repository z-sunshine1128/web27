from django.urls import path
from . import views

app_name = "zhaoyanchao"

urlpatterns = [
    path('index/',views.index,name="index")
]