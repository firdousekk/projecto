from django.urls import path
from . import views


urlpatterns=[
    path('home',views.home),
    path('viewstudent',views.viewstudent),
    path('addattendence',views.addattendence),
    path('profile',views.profile)
]