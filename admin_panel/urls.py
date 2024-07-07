from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('admin-panel/', views.admin_view, name='admin'),
    path('admin-contact/', views.contact_view_admin, name='admin-contact'),
    path('admin-teacher-list/', views.teacher_list_view, name='admin-teacher-list'),
    path('admin-child-group-list/', views.children_group_members_view, name='admin-child-group-list'),

    path('admin-contact/info/<int:pk>', views.contact_info_view, name='admin-contact-info'),
    path('admin-contact-delete/<int:pk>', views.contact_delete_view, name='admin-contact-delete'),
    path('admin-contact-create/>', views.contact_create_view, name='admin-contact-create'),
    path('admin-contact-edit/<int:pk>', views.contact_edit_view, name='admin-contact-edit'),


]
