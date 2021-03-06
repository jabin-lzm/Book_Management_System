"""Book_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
import notifications.urls
from book.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    re_path('^captcha/',include('captcha.urls')),
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', HomeView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('borrow/', BorrowView.as_view(), name='borrow'),
    path('return/', ReturnView.as_view(), name='return'),
    path('test/', TestView.as_view(), name='test'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    path('reset/<str:active_code>',ResetView.as_view(),name='reset'),
    path('modify/',ModifyView.as_view(),name='modify'),
    path('request/',RequestView.as_view(),name='request'),
    path('want/',WantView.as_view(),name='want'),
    path('notice/',CommentNoticeListView.as_view(),name='notice'),
    path('update/',CommentNoticeUpdateView.as_view(),name='update'),
    path('link/',LinkView.as_view(),name='link')
]