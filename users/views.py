from django.shortcuts import render

def login(request):
    context ={'title': 'GeekShop - Автризация'}
    return render(request, 'users/login.html', context)

def registration(request):
    context ={'title': 'GeekShop - Регистрация'}
    return render(request, 'users/registration.html', context)
