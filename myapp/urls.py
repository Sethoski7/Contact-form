from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_form, name='contact'),
    path('success/', views.success, name='success'),
]