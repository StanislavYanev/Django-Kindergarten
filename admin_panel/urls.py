from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('admin-panel/', views.admin_view, name='admin'),
    path('admin-contact/', views.contact_view_admin, name='admin-contact'),
    path('admin-teacher-list/', views.teacher_list_view, name='admin-teacher-list'),
    path('admin-child-group-list/', views.children_group_members_view, name='admin-child-group-list'),
    path('admin-search-parent/', views.search_child_parent, name='admin-search-parent'),
    path('admin-new-event/', views.new_event_view, name='admin-new-event'),
    path('admin-new-event-create/', views.new_event_create_view, name='admin-new-event-create'),
    path('admin-new-event-list/', views.new_event_list_view, name='admin-new-event-list'),
    path('admin-event-details/<int:pk>', views.event_details_view, name='admin-event-details'),
    path('admin-event-edit/<int:pk>', views.event_edit_view, name='admin-event-edit'),
    path('admin-event-send/<int:pk>', views.send_mail_for_event, name='admin-event-send'),
    path('admin-event-delete/<int:pk>', views.event_delete_view, name='admin-event-delete'),

    # path('admin-child-group-add-new/', views.children_group_add_child_view, name='admin-child-group-add-new'),
    path('admin-contact/info/<int:pk>', views.contact_info_view, name='admin-contact-info'),
    path('admin-contact-delete/<int:pk>', views.contact_delete_view, name='admin-contact-delete'),
    path('admin-contact-create/', views.contact_create_view, name='admin-contact-create'),
    path('admin-contact-edit/<int:pk>', views.contact_edit_view, name='admin-contact-edit'),

]

