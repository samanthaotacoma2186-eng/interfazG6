from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola, name='home'),
    path('book/', views.hola, name='book'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('donation/', views.donation, name='donation'),
    path('event/', views.event, name='event'),
    path('feature/', views.feature, name='feature'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard')

]