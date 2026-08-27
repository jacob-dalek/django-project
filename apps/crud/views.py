from django.shortcuts import render
from django.conf import settings
import os

def index(request):
    tink_images = os.listdir(os.path.join("C:/Users/jacob/Desktop/django-project/apps/crud/static/tink_images")) # string literal not great 
    context = {"title": "Home", "tink_images": tink_images}
    return render(request, "./crud/index.html", context)
