from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from myapp.models import Contact


# Create your views here.
def index(request):
    context = {
        "variable1": "Shahid is very innocent guy ",
        "variable2": "Ali bhai ki site h "
    }
    return render(request, 'index.html', context)
      #return HttpResponse("Hello Myapp views")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = contact(name=name, email=email, phone = phone, desc= desc, date=datetime.today())
        contact.save()
        return redirect('contact')
    return render(request, 'contact.html')

def carrier(request):
    return render(request, 'carrier.html')