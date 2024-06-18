from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('admin-panel/', views.admin_view, name='admin'),
    path('admin-contact/', views.contact_view_admin, name='admin-contact'),
]
