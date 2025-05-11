from django.shortcuts import render,redirect
from creditapp.models import credit_table 
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request,'index.html')

def creditcard(request):
    return render(request,"registerdemo.html")
    if request.method == 'POST':
        # if request.POST.get(container)
        name=request.POST['name']
        email=request.POST['email']
        phno=request.POST['phno']
        user=request.POST['user']
        password=request.POST['password']
        print(name,email,phno,user,password)
        obj=credit_table()
        obj.name = name.request.POST.get('name')
        obj.email = email.request.POST.get('email')
        obj.phno = phno.request.POST.get('phno')
        obj.user = user.request.POST.get('user')
        obj.password = password.request.POST.get('password')
        obj.save()
        messages.success(request,'registration successfully')
        return render(request,"registerdemo.html")
    else:
        return render(request,"registerdemo.html")
        # context={

        # }

def creditlogin(request):
    return render(request,'logindemo.html')

def log(request):
    return render(request,"logindemo.html")
    if request.method== 'POST':
        user=request.POST.get('user')
        password=request.POST.get('password')
        cr=credit_table.objects.filter(user=user,password=password)
        if cr:
            return redirect("dashboard")
        else:
            return render(request,"dashboard.html")
    else:
        return render(request,"logindemo.html")

def dashboards(request):
    return render(request,'dashboard.html')

def connect(request):
    return render(request,'dashboard.html')

def contact(request):
    return render(request,'contact.html')

# def creditcard(request):
#     return render(request,"registerdemo.html")
#     if request.method == 'POST':
#         name=request.POST['name']
#         email=request.POST['email']
#         phno=request.POST['phno']
#         user=request.POST['user']
#         password=request.POST['password']
#         print(name,email,phno,user,password)
#         obj.credit_table()
#         obj.name = name
#         obj.email = email
#         obj.phno = phno
#         obj.user = user
#         obj.password = password
#         obj.save()
#         context={

#         }
        # return render(request,"registerdemo.html")

	