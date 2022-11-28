from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'commen_templates/home.html')


def adminlogin(request):
    return render(request,'commen_templates/adminlogin.html')  



def studentlogin(request):
    return render(request,'commen_templates/studentlogin.html') 



def teacherlogin(request):
    return render(request,'commen_templates/teacherlogin.html') 


    
def views(request):
    return render(request,'commen_templates/views.html') 

def css(request):
    return render(request,'commen_templates/css.html')   

def css1(request):
    return render(request,'commen_templates/css1.html')     
        
    
    
      