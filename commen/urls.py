from  django.urls import path
from . import views
app_name='commen'

urlpatterns=[
    path('', views.home,name='index'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('studentlogin',views.studentlogin,name='studentlogin'),
    path('teacherlogin',views.teacherlogin,name='teacherlogin'),
    path('views',views.teacherlogin,name='views'),
    path('css',views.css,name='css'),
    path('css1',views.css1,name='css1')
    
]
