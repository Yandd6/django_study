from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        if username == "admin" and password == "123456":
            return HttpResponse("登录成功")
        else:
            return render(request, "index.html", {"error": "用户名或密码错误"})