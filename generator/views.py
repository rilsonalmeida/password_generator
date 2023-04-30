from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html', {'author': 'Rilson Almeida'})


def password(request):
    thepassword = ''
    
    characters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '1234567890'
    special_chars = '!@#$%¨¨&*()_+^~:></?°ªº{}[]'
    
    length = int(request.GET.get('length', 15))
    
    desired_options = list(characters)
    
    if request.GET.get('numbers'):
        desired_options.extend(numbers)
    
    if request.GET.get('uppercase'):
        desired_options.extend(characters.upper())
    
    if request.GET.get('special'):
        desired_options.extend(special_chars)
    
    for i in range(length):
        thepassword += random.choice(desired_options)
    
    return render(request, 'generator/password.html', {'password': thepassword})