from django.shortcuts import render,redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.core.mail import send_mail
from contact.forms import ContactForm


# Create your views here.


def log_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')
    else:
        form = ContactForm()
    return render(request, "contact/log-in-contacts.html", {'form': form})
