# BUZZ -> VIEWS.PY
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
