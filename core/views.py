from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from core.models import User, Habit

# def login(request):
#     return render(request, "core/login.html")

def dashboard(request):
    return render(request, "core/dashboard.html")