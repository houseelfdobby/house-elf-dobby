from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'SignupUser.html')

def userroom(request):
    return render(request, 'userroom.html')

