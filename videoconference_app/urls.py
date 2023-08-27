from django.urls import path
from . import views

urlpatterns=[
    path('',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('meetings/',views.videocall,name='meetings'),
    path('logout/',views.logout_view,name='logout'),
    path('join/',views.join_room,name='join_room'),
]