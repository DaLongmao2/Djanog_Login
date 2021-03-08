# 编写装饰器检查用户是否登录
import time

from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from Login.models import User, get_token, out_token
from Login.utils.email import send_email
from Pro import settings


def check_login(func):
    def inner(request, *args, **kwargs):
        # next_url = request.get_full_path()
        # 获取session判断用户是否已登录
        if request.session.get('is_login'):
            # 已经登录的用户...
            return func(request, *args, **kwargs)
        else:
            #   没有登录的用户，跳转刚到登录页面
            return redirect("login")
            # return redirect(reverse('profile', error =  "请先登录"))
    return inner



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        token = get_token(settings.TOKEN_KEY)
        t = time.localtime(time.time() + 300)

        text = f"""
        你好,{username}:
            效期为5分钟!http://{request.get_host()}/activate/{token}',请在{t[0]}年{t[1]}月{t[2]}日{t[3]}时{t[4]}分{t[5]}秒前激活！
        """
        html = f"""
        <h2>你好,<font color="blue">{username}</font>:</h2>
        <h3>&nbsp;&nbsp;链接有效期为5分钟! <a href='http://{request.get_host()}/activate/{token}'>点我激活并登录</a></h3>
        <h4>&nbsp;&nbsp;请在{t[0]}年{t[1]}月{t[2]}日{t[3]}时{t[4]}分{t[5]}秒前激活</h4>
        <h6>&nbsp;&nbsp;<font color="#8a2be2">如链接过期，请重新注册，返回 <a href=""><font color="red">主页</font></a> | <a href=""><font color="red">注册页面</font></a> </font></h6>
        """
        em = send_email("注册激活", html, text, [email])
        if em:
            return JsonResponse({'code' : 200})
        return JsonResponse({'code' : 300})
    return render(request, 'register.html')


def activate(request,   token):
    istoken = out_token(settings.TOKEN_KEY, token)
    if istoken:
        return redirect('login')
    else:
         return redirect('register')

# @csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # next_url = request.POST.get('next_url')
        remember_sign = request.POST.get("check")
        isuser = User.objects.filter(email=email).first()
        if isuser and check_password(password, isuser.password):
        # if email == '872039610@qq.com' and password == '123'r:
            request.session['user_info'] = {
                'email': email,
                'password': password,
                'username':isuser.username
            }
            request.session['is_login'] = True

            if remember_sign == 'on':
                request.session['is_remember'] = True
            else:
                request.session['is_remember'] = False

            # if next_url and next_url != 'logout/':
            #     response = redirect(next_url)
            # else:
            #     response = redirect('index')
            return redirect('index2')
        else:
            error_msg = '登录失败，请重试'
            return render(request, "login.html", {'error_msg': error_msg})

    # next_url = request.GET.get("next", '')
    # print(next_url)
    # 检查是否勾选了记住密码功能
    password, check_value = '', ''
    user_session = request.session.get('user_info', {})
    email = user_session.get('email', '')
    if request.session.get('is_remember'):
        password = user_session.get('password', '')
        check_value = 'checked'
    return render(request, "login.html", {
        # 'next_url': next_url,
        'email': email,
        'password': password,
        'check_value': check_value
    })


def logout(request):
    rep = redirect("login")
    # request.session.delete()
    # 登出，则删除掉session中的某条数据
    if 'is_login' in request.session:
        del request.session['is_login']
    return rep


@check_login
def index(request):
    return render(request, "index.html")


# @check_login
def index2(request):
    if request.method == 'POST':
        box = request.POST.getlist('checkboxBtn')
        for b in box:
            user = User.objects.get(id=b)
            user.isdelete = True
            user.save()
            return redirect('index2')
    return render(request, 'index2.html', {"user_all" : User.objects.all().filter(isdelete=False)})


@check_login
def test(request):
    User.objects.create(email='872039610@qq.com', password='123456', username='张三')
    User.objects.create(email='5772027@qq.com', password='123456', username='李四')
    User.objects.create(email='1232143546@qq.com', password='123456', username='王麻子')
    User.objects.create(email='1546123477@qq.com', password='123456', username='袁滨心')
    return HttpResponse('测试数据添加完成')

