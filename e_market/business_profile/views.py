from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def show_profile (request, name):
    return render(request, "profile.html", {"heading" : f"View {name}'s Profie"})
    