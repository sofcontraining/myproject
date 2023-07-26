from django.shortcuts import render, HttpResponse, redirect
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
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        dept = request.POST['dept']
        image = request.FILES['image']
        empdetails = Member(fname=fname, lname=lname, age=age, dept=dept, image=image)
        empdetails.save()
        return redirect('/members')
    return render(request, 'contact.html')