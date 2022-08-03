from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

post = [
    {
        'img_link':'/feed/apollo9.jpg',
        'img_caption':'have a great day',
        'like_count': '117'
    },
    {
        'img_link':'/feed/apollo17.jpg',
        'img_caption':'have a great day',
        'like_count': '13'
    },
    {
        'img_link':'/feed/interstelar.png',
        'img_caption':'have a great day',
        'like_count': '128'
    },
    {
        'img_link':'/feed/pyramidsgiza.jpg',
        'img_caption':'have a great day',
        'like_count': '1'
    },
    {
        'img_link':'/feed/margert.jpg',
        'img_caption':'have a great day',
        'like_count': '11'
    }
    
]

def index(request):
    context = {
        'posts':post
    }
    return render(request, 'index.html', context)
   

def my_post(request):
    context = {
        'posts':post
    }
    return render(request, 'my_post.html', context)

def logout_page(request):
    return render(request, 'logout_page.html')

def create_new(request):
    return render(request, 'create_new.html')

def login_page(request):
    return render(request, 'login_page.html')
