import json
from tkinter import PhotoImage

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import Upload


# Create your views here.
def photo_upload_view(request):
  
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UploadForm()
    return render(request, 'main.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')


def get_all_photos(request):
    objects = Upload.objects.all()
    all_photos = []
    for photo in objects:
        all_photos.append(dict(
            id = str(photo.photo_id),
            upload_datetime = str(photo.upload_datetime),
            path = str(photo.photo.url)[1:]
        ))
    return render(request, 'all_photos.html',{'photos' : all_photos})


@csrf_exempt
def delete_photo(request):

    if request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        delete_id = body.get('id')
        Upload.objects.filter(photo_id=delete_id).delete()

    return HttpResponse('successfully deleted photo')
