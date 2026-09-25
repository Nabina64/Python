from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    context = {
        'title': 'Home Page',
        'message': 'Welcome to the Home Page!',
    }
    return render(request, 'index.html', context)
def contact(request):
    context = {
        'title': 'Contact Us',
        'message': 'This is the contact page.',
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'title': 'About Us',
        'message': 'This is the about page.',
    }
    return render(request, 'about.html', context)

def home(request):
    context = {
        'title': 'Home Page',
        'h1': 'Welcome to the Home Page!',
        'message': 'This is the home page of our Django application.',
    }
    return render(request, 'index.html', context)
