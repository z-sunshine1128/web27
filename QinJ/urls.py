from . import views
from django.urls import path

app_name = 'QinJ'

urlpatterns = [
    path('index/',views.index,name='index')
]