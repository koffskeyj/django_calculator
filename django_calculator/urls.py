"""django_calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from calculator import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.calculator_view, name="calculator_view"),
    url(r'^login/$', login, name="home_view"),
    url(r'^logout/$', logout, name="logout_view"),
    url(r'^user_create/$', views.user_create_view, name="user_create_view"),
    url(r'^accounts/profile/$', views.profile_view, name="profile_view"),
    url(r'^calculator/$', views.calculator_view, name="calculator_view")

]
