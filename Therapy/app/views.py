from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')



