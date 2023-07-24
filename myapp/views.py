from django.shortcuts import render, HttpResponse
from . models import Member 

# Create your views here.
def home(request):
    # return HttpResponse("This is my home page")
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def member(request):
    all_members = Member.objects.all()
    return render(request, 'members.html', {'members':all_members})

def contact(request):
    return render(request, 'contact.html')