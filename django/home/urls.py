from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'), 
    path('root/', views.root, name='root'), 
    path('base/', views.base, name='base'),
    
]
