from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models


# Create your views here.


def welcome(request):  # request 封装了用户请求的所有内容
    return HttpResponse("my first django today")


def main(request):
    return render(request, "main.html", )


def login(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # 添加数据到数据库
        models.UserInfo.objects.create(user=username, pwd=password)

    # 从数据库读取数据
    user_list = models.UserInfo.objects.all()
    return render(request, "login.html", {"data": user_list})
