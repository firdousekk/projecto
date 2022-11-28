from django.urls import path
from . import views
app_name='school_admin'


urlpatterns=[
    path('home',views.home,name='index'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('viewstudent',views.viewstudent,name='viewstudent'),
    path('viewattendence',views.viewattendence,name='viewattendence')
  
]