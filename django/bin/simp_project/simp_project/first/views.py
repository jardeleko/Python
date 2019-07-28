from django.shortcuts import render
from django.http import HttpResponse
from django import template 

def index(request):
	return render(request, 'index.html')

def pag(request):
	return render(request, 'cadaster.html') 
# Create your views here.
def details(request):
	return render(request, 'details.html')