from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    #return HttpResponse('Hello WORLD!!!!')
    return render(request, 'generator/home.html', {'password':'thisispassword'})
#
# def eggs(request):
#     return HttpResponse('These are my eggs!!!!!!!!!!!')

def password(request):

    thepassword=''
    characters=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length',12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('specialchars'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    for x in range(length):
        thepassword += random.choice(characters)



    return render(request, 'generator/password.html',{'password':thepassword})


def about(request):
    return render(request, 'generator/about.html')
