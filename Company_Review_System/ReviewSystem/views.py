from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from .models import Detail, Userdata,Image,Co,Contacts


# Create your views here.

def signup(request):
    if request.method == "POST":
        Email = request.POST.get('Email')
        Uname = request.POST.get('Uname')
        Password = request.POST.get('Password')
        obj = Detail(email=Email, uname=Uname, password=Password)
        obj.save()
        return redirect("/login")
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        Uname = request.POST.get('Uname')
        Password = request.POST.get('Password')
        count = Detail.objects.filter(uname=Uname, password=Password).count()
        if count > 0:
            return redirect("/index")

    return render(request, "login.html")


def index(request):
    data = Userdata.objects.all
    if request.method == "POST":
        Title = request.POST['Title']
        File = request.FILES['File']
        Description = request.POST['Description']
        Post = request.POST['Post']
        obj = Userdata(title=Title, img=File, description=Description, post=Post)
        obj.save()
    return render(request, "index.html", {"data": data})

def header(request):
    return render(request,"header.html")
def footer(request):
    return render(request,"footer.html")

def reviews(request, id):
    data = Userdata.objects.get(id=id)
    dt = Userdata.objects.all
    c = Co.objects.filter(pid=id)
    if request.method == "POST":
        n = request.POST['user']
        m = request.POST['msg']
        obj = Co(nm=n,msg=m)
        obj.pid_id = id
        obj.save()

    return render(request, "reviews.html",{"data":data,"c":c,"dt":dt,"id":id})

def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method == "POST":
        obj = Contacts(Name=request.POST['name'],Email=request.POST['email'],Msg=request.POST['message'])
        obj.save()
    return render(request,"contact.html")
def logout(request):
    return render(request,"login.html")


