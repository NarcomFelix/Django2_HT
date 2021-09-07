from django.shortcuts import render

from users.models import User

def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/index.html', context)

#Read
def admin_users(request):
    context = {'title': 'GeekShop - Пользователи', 'users': User.objects.all()}
    return render(request, 'admins/admin-users.html', context)