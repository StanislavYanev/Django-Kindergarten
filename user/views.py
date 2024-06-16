from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def sing_in(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("gallery:gallery")
    else:
        form = UserCreationForm()

    return render(request, 'user/sing-in.html', {"form": form})


def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("gallery:gallery")
    else:
        form = AuthenticationForm()
    return render(request, 'user/log-in.html', {"form": form})


def log_out(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")