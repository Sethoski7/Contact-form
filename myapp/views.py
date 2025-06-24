from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Contact

def contact_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('success')
    
    return render(request, 'myapp/contact_form.html')

def success(request):
    return render(request, 'myapp/success.html')