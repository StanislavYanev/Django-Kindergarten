from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from contact.forms import ContactForm
from contact.models import Contact


@staff_member_required
def admin_view(request):
    return render(request, 'admin_panel/admin-panel.html')


@staff_member_required
def contact_view_admin(request):
    contacts = Contact.objects.all()
    return render(request, 'admin_panel/admin-contact.html', {"contacts": contacts})
