from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'school_admin_templates/home.html')
def addstudent(request):
    return render(request,'school_admin_templates/addstudent.html')  
def viewstudent(request):
    return render(request,'school_admin_templates/viewstudent.html') 
def viewattendence(request):
    return render(request,'school_admin_templates/viewattendence.html')         