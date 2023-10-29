from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    if request.user.is_authenticated:
        return redirect('view-history')
    else:
        return redirect('login')

@login_required
def viewHistory(request):
    history = request.user.history.all()
