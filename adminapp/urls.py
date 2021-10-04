from django.urls import path
# from adminapp.views import index, admin_users, admin_users_create, admin_users_update, admin_users_delete
from adminapp.views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('authapp/', UserListView.as_view(), name='admin_users'),
    path('authapp-creat/', UserCreateView.as_view(), name='admin_users_create'),
    path('authapp-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('authapp-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
]