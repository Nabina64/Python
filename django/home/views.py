from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    context = {
        'title': 'Index',
        'heading': ' Home Page',
        'message': 'Welcome to the Home Page!',
        'students': [
    {
        "name": "Nabina",
        "age": 20,
        "contact": "9800000000"
    },
    {
        "name": "Ram",
        "age": 21,
        "contact": "9811111111"
    },
    {
        "name": "Sita",
        "age": 19,
        "contact": "9822222222"
    }
]
    }
    return render(request, 'home/index.html', context)
def contact(request):
    context = {
        'title': 'Contact Us',
        'message': 'This is the contact page.',
    }
    return render(request, 'home/contact.html', context)

def about(request):
    context = {
        'title': 'About Us',
        'message': 'This is the about page.',
    }
    return render(request, 'home/about.html', context)

def root(request):
    context = {
        'title': 'Root Page',
        'message': 'This is the root page.',
    }
    return render(request, 'home/root.html', context)
def base(request):
    context = {
        'title': 'Base Page',
        'message': 'This is the base page.',
    }
    return render(request, 'home/base.html', context)

