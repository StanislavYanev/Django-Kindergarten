from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def admin_view(request):
    return  render(request, 'admin_panel/admin-panel.html')