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


    
def minmaster(request):
    return render(request,'commen_templates/minmaster.html') 

def css(request):
    return render(request,'commen_templates/css.html')   

def css1(request):
    return render(request,'commen_templates/css1.html')    

def css2(request):
    return render(request,'commen_templates/css2.html')   

def css3(request):
    return render(request,'commen_templates/css3.html')    
        
    
     
        
    
    
      