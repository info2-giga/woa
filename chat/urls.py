from django.urls import path
from . import views

urlpatterns = [
    path('<str:room>/', views.room, name='room'),
    path('chatlist/checkview/', views.checkview, name='checkview'),
    path('chatlist/checkviewGet/', views.checkview_get, name='checkviewGet'),
    path('chatlist/<str:sender>/', views.home, name='ligma'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('getRooms/<str:user>/', views.getRooms, name='getRooms'),
    path('block', views.block_room, name='block_room')
]