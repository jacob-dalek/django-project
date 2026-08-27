from django.shortcuts import render
from django.conf import settings
import os

def index(request):
    context = {"title": "Home"}
    return render(request, "./crud/index.html", context)
