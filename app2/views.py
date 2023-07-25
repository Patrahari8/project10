from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def thrid(request):
    return render(request, 'third.html')
def fourth(request):
    return render(request, 'fourth.html')
def string2(request):
    return HttpResponse('<h1> app2 string')