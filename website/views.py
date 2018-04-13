from django.shortcuts import render
from tender_details.models import tender

def homePage_view(request):
    tenders = tender.objects.all()
    return render(request, 'pages/index.html', {'tenders' : tenders})

def aboutUs_view(request):
    return render(request, 'pages/about_us.html')

def network_view(request):
    return render(request, 'pages/network.html')