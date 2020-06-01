from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'matt r',
        'title': 'blog post 1',
        'content': 'this is some content',
        'date_posted': 'August 27th, 2018'
    },
    {
        'author': 'matt randall',
        'title': 'blog post 2',
        'content': 'this is some content',
        'date_posted': 'August 27th, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'sales_performance/home.html', context)

def data_management(request):
    return render(request, 'sales_performance/data_management.html', {'title': 'Data Management'})
