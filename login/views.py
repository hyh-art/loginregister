from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    pass
    return render(request,'login/index.html')   #render租用html模板,参数：请求，模板的名字
def login(request):
    pass
    return render(request,'login/login.html')
def register(request):
    pass
    return render(request,'login/register.html')
def  logout(request):
    pass
    return redirect('/login/')    #redirect  重定向
