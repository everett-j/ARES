# Create your views here.
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

    
def index(request):
    return render(request, 'chatter_box/index.html')

