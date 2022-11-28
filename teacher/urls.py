from django.urls import path
from . import views
app_name='teacher'


urlpatterns=[
    path('home',views.home,name='index'),
    path('viewstudent',views.viewstudent),
    path('addattendence',views.addattendence),
    path('profile',views.profile)
]