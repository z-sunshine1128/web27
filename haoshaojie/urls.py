from django.urls import path
from . import views

app_name = "haoshaojie"

urlpatterns = [
    path('index/',views.index,name="index")
]
