from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required
from contact.forms import ContactForm
from contact.models import Contact
from user.models import Teacher
from django.contrib.auth.models import User


@login_required
@permission_required("user.can_view_admin_panel")
def admin_view(request):
    return render(request, 'admin_panel/admin-panel.html')


@login_required
def contact_view_admin(request):
    contacts = Contact.objects.all()
    return render(request, 'admin_panel/admin-contact.html', {"contacts": contacts})


@login_required
def contact_info_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'admin_panel/contact-details.html', {"contact": contact})


@login_required
def contact_create_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:admin-contact')
    else:
        form = ContactForm()
    return render(request, 'contact/log-in-contacts.html', {'form': form})


@login_required
def contact_edit_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(instance=contact)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            print("POST")
            return redirect('admin_panel:admin-contact')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'admin_panel/admin-contact-edit.html', {"contact": contact, "form": form})


@login_required
def contact_delete_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('admin_panel:admin-contact')
    return render(request, 'admin_panel/admin-contact-delete.html', {'contact': contact})


@login_required
@permission_required("user.view_teacher")
def teacher_list_view(request):
    teachers = Teacher.objects.all()
    return render(request, 'admin_panel/teacher-list.html', {"teachers": teachers})






