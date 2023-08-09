"""
URL configuration for CompanyReviewSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from ReviewSystem import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("index",views.index, name="index"),
    path("login",views.login, name="login"),
    path("",views.signup, name="signup"),
    path("header",views.header, name="header"),
    path("footer",views.footer, name="footer"),
    path("about",views.about, name="about"),
    path("contact",views.contact, name="contact"),
    path("logout", views.logout, name="logout"),
    path("reviews/<int:id>",views.reviews),


] + static(settings.DIR,document_root=settings.DIR_NAME) + static("Static/",document_root="Static")
