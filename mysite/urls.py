"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# Importing from Django library
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
<<<<<<< HEAD
    path(
        # Home page
        '', 
        TemplateView.as_view(template_name="index.html"), 
        name='home'
        ),
    path(
        # Recipes app
        'recipes/',
        include('recipes.urls'), 
        name='recipes'
        ),
    path(
        # AllAuth Account app
        'accounts/', 
        include('allauth.urls'), 
        name='allauth'
        ),
    path(
        # Django Admin app
        'admin/',
        admin.site.urls,
        name='admin'
        ),
    path(
        # AllAuth Logout app
        'logout',      
        LogoutView.as_view(), 
        name='logout'
        ),
=======
    path('xDBEGesUy01DKCYZWH8W/', admin.site.urls),     # obscure admin path
    path('recipes/', include('recipes.urls'), name='recipes'),

    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
>>>>>>> 27e9fbe8441b19049f02c6b3e48f9e5d02071f6c
]

