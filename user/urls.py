from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('sing-in/', views.sing_in, name='sing-in'),
    path('log-in/', views.log_in, name='log-in'),
    path('log-out/', views.log_out, name='log-out'),
]