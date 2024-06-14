from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('sing-in/', views.sing_in, name='sing-in'),
]