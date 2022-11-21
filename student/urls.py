from django.urls import path
from . import views


urlpatterns=[
    path('home',views.home,name='index'),
    path('profile',views.profile),
    path('changepassword',views.changepassword),
    path('viewattendence',views.viewattendence)
]