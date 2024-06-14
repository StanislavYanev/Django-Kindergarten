from django.shortcuts import render, redirect
from .models import GalleryImage
from .forms import GalleryForm
from django.http import HttpResponse

# Create your views here.

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery/gallery.html', {"images": images})


def image_view(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:gallery')

    else:
        form = GalleryForm()
    return render(request, 'gallery/image-form.html', {'form': form})
