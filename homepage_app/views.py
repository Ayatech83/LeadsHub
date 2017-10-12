from django.shortcuts import render
from homepage_app.models import Company
# Create your views here.

def index(request):
	return render(request, 'pages/index.html')