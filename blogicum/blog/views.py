from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    template = 'blog/index.html'
    return render(request, template)

def post_detail(request):
    pass

def category_posts(request):
    pass