from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2_first(request):
    return HttpResponse('this is 1st view of app2')

def app2_second(request):
    return HttpResponse('this is 2nd view of app2')