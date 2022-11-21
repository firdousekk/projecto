from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'teacher_templates/home.html')
def viewstudent(request):
    return render(request,'teacher_templates/viewstudent.html')  
def addattendence(request):
    return render(request,'teacher_templates/addattendence.html') 
def profile(request):
    return render(request,'teacher_templates/profile.html')         