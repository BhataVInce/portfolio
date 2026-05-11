from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
import json

def entreprise(request):
    path = staticfiles_storage.path("files/texte.json")
    with open(path, "r") as f:
        data = json.load(f)
    return render(request, "entreprise.html", {"data": data["Entreprise"]})