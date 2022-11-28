from django.urls import path
from . import views
app_name='student'


urlpatterns=[
    path('home',views.home,name='index'),
    path('profile',views.profile),
    path('changepassword',views.changepassword),
    path('viewattendence',views.viewattendence)
]