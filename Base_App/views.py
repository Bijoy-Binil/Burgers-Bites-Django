from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    menu=ItemList.objects.all()
    objs=Items.objects.all()[:3]
    review=Feedback.objects.all()
    context={'menu':menu,'objs':objs,'review':review}

    return render(request,'home.html',context)

def aboutView(request):
    data=AboutUs.objects.all()
    return render(request,'about.html',{'data':data})

def menuView(request):
    menu=ItemList.objects.all()
    objs=Items.objects.all()
    context={'menu':menu,'objs':objs}
    return render(request,'menu.html',context)

def bookTableView(request):
    if request.POST:
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        persons=request.POST.get('persons')
        date=request.POST.get('date')

        if username!="" and phone!="" and email!="" and persons!=0 and date!="":
            data=BookTable(Name=username,
                           Phone_number=phone,
                           Email=email,
                           Total_person=persons,
                           Booking_date=date)
            data.save()
            
    
    return render(request,'book_table.html')

def feedback(request):
    
    if request.POST:
        username=request.POST.get('username')
        description=request.POST.get('description')
        rating=request.POST.get('rating')
        image=request.FILES.get('image')
        data=Feedback(User_name=username,
                      Description=description,
                      Rating=rating,
                      Image=image)
       
        data.save()               

    return render(request,'feedback.html')


