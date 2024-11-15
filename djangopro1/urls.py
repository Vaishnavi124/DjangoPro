"""
URL configuration for djangopro1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from myapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main,name='main'),
    path('home/',home,name='home'),
    path('register/',register,name='register'),
    path('login/',loginview,name='loginview'),
    path('logout/',logoutview,name='logoutview'),
    path('courses/',courses,name='courses'),
    path('cart/', cart, name='cart'),
    path('add_to_cart/<int:course_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_id>/', remove_from_cart, name='remove_from_cart'),
    path('delete/', delete_cart, name='delete_cart'),
    path('profile/',profile,name='profile'),
    path('search/',search_item,name='search_item')
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
