from django.shortcuts import render
from .models import tender

def tender_view(request):
    tenders = tender.objects.all()
    return render(request, 'tender.html', {'tenders': tenders})
