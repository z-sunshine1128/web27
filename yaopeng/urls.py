from django.urls import path
from . import views

app_name = "yaopeng"

urlpatterns = [
    path('index/',views.index,name="index")
]
