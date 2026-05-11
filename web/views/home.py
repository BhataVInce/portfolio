from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
import json

def homeview(request):
    return render(request, "home.html", {"test": "testoui"})

def mission(request):
    path = staticfiles_storage.path("files/texte.json")
    with open(path, "r") as f:
        data = json.load(f)
    return render(request, "mission.html", {"data": data["Mission"]})

def epreuve(request):
    path = staticfiles_storage.path("files/texte.json")
    with open(path, "r") as f:
        data = json.load(f)
    return render(request, "epreuve.html", {"data": data["Epreuve"]})