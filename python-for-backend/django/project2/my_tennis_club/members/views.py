from django.shortcuts import render
from django.http import HttpResponse

def myview01(request):
    return HttpResponse("Hello world!")

#But how can we execute the view? Well, we must call the view via a URL.

