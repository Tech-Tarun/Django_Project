from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Details
from task_app.forms import SaveDetails

def index(request):
    return render(request,'index.html')

def logout(request):
    return render(request,'logout.html')

def signup(request):
    if request.method=='POST':
        form = SaveDetails(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        uname=request.POST['uname']
        psw=request.POST['psw']
        det=Details.objects.all()
        lis=[]
        k=0
        for i in det:
            if i.user==uname and i.pas==psw:
                lis.append(i.id)
                lis.append(i.user)
                lis.append(i.email)
                lis.append(i.add)
                lis.append(i.add1)
                lis.append(i.city)
                lis.append(i.state)
                lis.append(i.zip)
                print(lis)
                k=1
                return render(request, "details.html",{'detail':lis})
        if(k==0):
            return render(request, "index.html")
    else:
        return render(request, "index.html")
        


def screen3(request):
    det=Details.objects
    print(det)
    return render(request, "details1.html",{'detail':det})

def delete(request,id):
    det=Details.objects.get(pk=id)
    det.delete()
    return redirect('/')


def edit(request,id):
    if request.method=='POST':
        det=Details.objects.get(pk=id)
        form = SaveDetails(request.POST or None, instance = det)
        if form.is_valid():
            print("DOne")
            form.save()
        return redirect('/')
    else:
        print("unDOne          \t \t\t\tktltlt")
        det=Details.objects.get(pk=id)
        return render(request, "details.html",{'detail':det})