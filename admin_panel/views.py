from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from contact.forms import ContactForm
from contact.models import Contact
from user.models import Teacher, Parent
from guardian.shortcuts import get_objects_for_user
from user.models import ChildrenGroup, Child
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models import Prefetch
from .forms import ChildForm, SearchChildForm


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


@login_required
@permission_required("user.can_view_children_group")
def children_group_members_view(request):
    try:
        children_group_qs = get_objects_for_user(request.user, 'user.can_view_strawberry_group', klass=ChildrenGroup)
        children_group_prefetch = Prefetch('children_group', queryset=children_group_qs,
                                           to_attr='prefetched_children_groups')
        children = Child.objects.filter().prefetch_related(children_group_prefetch)
        child_in_group = []
        for num in range(0, len(children_group_qs)):
            for child in children:
                if children_group_qs[num] == child.prefetched_children_groups:
                    child_in_group.append(child)
        return render(request, "admin_panel/child-group-list.html", {"children": child_in_group})

    except Exception as e:
        print(f"Error in children_group_members_view: {e}")
        return redirect("admin_panel:admin-list")


# This need more functionality on Parent-Child model to work properly
# @login_required
# @permission_required("user.can_view_children_group")
# def children_group_add_child_view(request):
#     children_group_qs = get_objects_for_user(request.user, 'user.can_view_strawberry_group', klass=ChildrenGroup)clear
#     if request.method == 'POST':
#         form = ChildForm(request.POST)
#         form.children_group = children_group_qs[0]
#         if form.is_valid():
#             form.save()
#             return redirect('admin_panel:admin-contact')
#     else:
#         form = ChildForm()
#     return render(request,"", {"form": form})


@login_required
def parent_group_members_view(request):
    all_parent = Parent.objects.all()


@login_required
def search_child_parent(request):
    form = SearchChildForm()
    results = []
    if 'query' in request.GET:
        form = SearchChildForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Child.objects.filter(last_name__icontains=query)
    print(request)
    # print(form)
    return render(request, "admin_panel/search-parent.html", {"form": form, "results": results})


@login_required
def new_event_view(request):
    return render(request, 'admin_panel/admin-panel-new-event.html')
