from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is my home page")
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')