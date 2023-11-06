

# Create your views here.
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import SharedFile
from django.utils.crypto import get_random_string
from django.views.generic import CreateView,TemplateView

class IndexView(TemplateView):
    template_name="file_sharing/index.html"
    

def upload_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            unique_identifier = get_random_string(length=10)
            form.instance.unique_identifier = unique_identifier
            form.save()
            return redirect("share-link",unique_identifier=unique_identifier)
    else:
        form = FileUploadForm()
    return render(request, "file_sharing/upload_file.html", {"form": form})

def share_link(request,unique_identifier):
    shared_file = SharedFile.objects.get(unique_identifier=unique_identifier)
    shared_file = SharedFile.objects.get(unique_identifier=unique_identifier)
    
    return render(request, "file_sharing/share_link.html", {"shared_file": shared_file})
