from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fifth(request):
    return render(request,'fifth.html')
def sixth(request):
    return render(request,'sixth.html')
def string3(request):
    return HttpResponse('<h1> string3 app3</h1>')