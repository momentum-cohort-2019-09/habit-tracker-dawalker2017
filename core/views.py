from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from core.models import User, Log, Habit
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.forms import ModelForm, inlineformset_factory
from core.forms import LogForm

def index(request):
    return render(request, 'core/index.html')

def register(request):
    return render(request, 'core/register.html')

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

@login_required
def log(request):
    return render(request, 'core/log.html')

@login_required
def habits(request):
    return render(request, 'core/habits.html')

def add_log(request, pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = user
            log.save()
            return redirect(to='dashboard')
    else:
        form = LogForm()

    return render(request, "core/add_log.html", {"form": form})

@csrf_exempt
def delete_log(request, pk):
    log = get_object_or_404(Log, pk=pk)
    if request.method == "POST":
        log.delete()
        return redirect(to='dashboard')
    return render(request, 'core/dashboard.html')
