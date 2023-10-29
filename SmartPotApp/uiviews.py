from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    if request.user.is_authenticated:
        return redirect('history')
    else:
        return redirect('login')

@login_required
def viewHistory(request):
    history = request.user.history.all()
    return render(request, 'history.html', 
    {
        'history': history, 
        'moisture_trend': [float(h.moisture) for h in history[:15]], 
        'timestamps': [(h.timestamp).strftime('%I:%M:%S') for h in history[:15:-1]]
    })
