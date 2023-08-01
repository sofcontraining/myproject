from django.shortcuts import render, HttpResponse
from myblog.models import Post

# Create your views here.

def bloghome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request,'bloghome.html', context)