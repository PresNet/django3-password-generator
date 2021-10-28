from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.

def about(request):
    thedate = str(datetime.now().time())
    return render(request, 'generator/about.html',{'date':thedate})


def home(request):
    return render(request, 'generator/home.html', {'password':'horujnvadff$'})


def password(request):
    thepassword = ""

    characters = list('abcdefghijklmnopqrstuvxyz')
    length = int(request.GET.get('length'))
    uppercase = request.GET.get('length')
    numbers = request.GET.get('numbers')
    specialcharacters = request.GET.get('specialcharacters')

    if uppercase:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVXYZ'))

    if numbers:
        characters.extend(list('0123456789'))

    if specialcharacters:
        characters.extend(list('^&$%#$@@#@^&^&**&&%'))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
