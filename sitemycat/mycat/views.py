from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from  django.shortcuts import render
import os
from django.conf import settings





# Create your views here.


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'mycat/index.html', data)


def video(request):
    return render(request, 'mycat/video.html')


def photo(request):
    image_dir = r'D:\Python\mycat\sitemycat\mycat\static\mycat\image\photos'
    images = os.listdir(image_dir)
    print(images)

    return render(request, 'mycat/photo.html', {'images': images})


def page_not_found(request, exception):
    return HttpResponseNotFound('Not found123123132')
