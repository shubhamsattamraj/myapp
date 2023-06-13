from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .models import UploadedFile
from .forms import FileUploadForm


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        content_type = ""
        if len(uploaded_file.name.split("."))>1:
            content_type = uploaded_file.name.split(".")[-1]
        model_file = UploadedFile.objects.create(file=uploaded_file, name=uploaded_file.name, content_type=content_type)
        model_file.save()
        return redirect('view_files')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})


def view_files(request):
    files = UploadedFile.objects.all()
    return render(request, 'views.html', {'files': files})
