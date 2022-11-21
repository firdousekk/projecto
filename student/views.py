from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'student_templates/home.html')
def profile(request):
    return render(request,'student_templates/profile.html')  
def changepassword(request):
    return render(request,'student_templates/changepassword.html') 
def viewattendence(request):
    return render(request,'student_templates/viewattendence.html')         