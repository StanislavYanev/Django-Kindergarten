from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def sing_in(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gallery:gallery")
    else:
        form = UserCreationForm()

    return render(request, 'user/sing-in.html', {"form": form})

