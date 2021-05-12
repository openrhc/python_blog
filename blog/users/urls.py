# users 子应用的视图路由

from django.urls import path
from users.views import RegisterView
from users.views import ImageCodeView
from users.views import SmsCodeView
from users.views import LoginView

urlpatterns = [
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('register/',RegisterView.as_view(),name='register'),

    # 图形验证码
    path('imagecode/', ImageCodeView.as_view(),name='imagecode'),

    # 短信验证码
    path('smscode/', SmsCodeView.as_view(),name='smscode'),

    # 登录
    path('login/', LoginView.as_view(),name='login'),
]