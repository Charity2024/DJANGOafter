from django.urls import path
from Myapp import views

urlpatterns = [
    path('welcome/', views.karibu),
    path('', views.myhome, name='my_index'),
    path('about/', views.about, name='my_about'),
    path('gallery/', views.gallery, name='my_gallery'),
    path('services/', views.services, name='my_services'),
    path('contact/', views.contact, name='my_contact')

]
