from django.urls import path
from . import views

app_name = "songjialun"

urlpatterns = [
    path('index/',views.index,name="index")
]
