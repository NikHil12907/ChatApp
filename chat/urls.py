from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.login_view, name='login' ),
    path('accounts/register/', views.register_view, name='register' ),
    path('logout/', views.logout_view, name='logout'),
    path('rooms/', views.room_list, name='room_list'),
    path('room/delete/<str:room_name>/', views.delete_room, name='delete_room'),
    path('create/', views.create_room, name='create_room'),
    path('<str:room_name>/', views.room, name='room'),
    

]
