from django.shortcuts import render, redirect
from .models import Hirecoder
from django.contrib import messages

# Create your views here.
def hire(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        coder_id = request.POST['coder_id']
        coder_name = request.POST['coder_name']
        email = request.POST['email']
        city = request.POST['city']
        phone = request.POST['phone']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']

    coder = Hirecoder(first_name = first_name, last_name = last_name, 
                      coder_id = coder_id, coder_name = coder_name, email = email, city = city, 
                      phone = phone, state = state, message = message, user_id = user_id)
    
    coder.save()
    messages.success(request, 'Thanks for reaching out')
    return redirect('coders_home')
