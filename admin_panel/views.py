from django.shortcuts import render, get_object_or_404, redirect
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


@staff_member_required
def contact_info_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'admin_panel/contact-details.html', {"contact": contact})



@staff_member_required
def contact_delete_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('admin_panel:admin')
    return render(request, 'admin_panel/admin-contact-delete.html', {'contact': contact})
