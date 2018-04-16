from django.shortcuts import render
from tender_details.models import tender

def homePage_view(request):
    tenders = tender.objects.all()
    return render(request, 'pages/index.html', {'tenders' : tenders})

def tenders_view(request):
    return render(request, 'pages/tenders.html')

def network_view(request):
    return render(request, 'pages/network.html')

def pricing_view(request):
    return render(request, 'pages/pricing.html')