from django.shortcuts import render
from django.conf import settings
import os

def index(request):
    folder = os.listdir(os.path.join("C:/Users/jacob/Desktop/django-project/apps/crud/static/tink_images")) # string literal not great 

    for files in folder:
        print(files)

    context = {"title": "Home"} 
    return render(request, "./crud/index.html", context)
