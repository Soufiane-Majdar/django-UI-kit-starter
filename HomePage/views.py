from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect
# Create your views here.

def home(request):
    title="Home"
    return render(request,'home/home.html',{'title':title})

def template(request):
    title="template"
    return render(request,'home/template.html',{'title':title})



def error_404_view(request, exception):
    return render(request, 'home/404.html')