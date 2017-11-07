from django.shortcuts import render
from django.http import HttpResponse

def homePage_view(request):
	return render(request, 'pages/index.html')

def aboutUs_view(request):
    return render(request, 'pages/about_us.html')

def network_view(request):
    return render(request, 'pages/network.html')