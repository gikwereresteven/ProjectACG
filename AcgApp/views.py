from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactTable
from .forms import ContactForm

# Create your views here.
def imbuto(request):
    return render(request, '../../acg/templates/imbuto.html', {'imbuto': imbuto})

def imishwi(request):
    return render(request, '../../acg/templates/imishwi.html',{'imishwi': imishwi})

def ifumbire(request):
    return render(request, '../../acg/templates/ifumbire.html',{'ifumbire': ifumbire})

def contact(request):
    return render(request, '../../acg/templates/contact.html',{'contact':contact})    