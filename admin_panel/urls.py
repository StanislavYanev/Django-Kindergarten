from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('admin-panel/', views.admin_view, name='admin'),
    path('admin-contact/', views.contact_view_admin, name='admin-contact'),
    path('admin-contact/info/<int:pk>', views.contact_info_view, name='admin-contact-info'),
    path('admin-contact-delete/<int:pk>', views.contact_delete_view, name='admin-contact-delete'),
]
