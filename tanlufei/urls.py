from django.urls import path
from . import views

app_name = "tanlufei"

urlpatterns = [
    path('index/',views.index,name="index")
]