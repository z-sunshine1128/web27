from django.urls import path
from . import views

app_name = "zhaolong"

urlpatterns = [
    path('index/',views.index,name="index")
]
