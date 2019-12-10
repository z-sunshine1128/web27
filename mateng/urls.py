from django.urls import path
from . import views

app_name = 'mateng'

urlpatterns = [
    path('index/',views.index,name='index')
]