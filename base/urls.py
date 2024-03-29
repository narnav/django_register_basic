"""
URL configuration for myproj project.

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

from base import views
# from rest_framework_simplejwt.views import TokenObtainPairView



urlpatterns = [
    path('',views.index ),
    path('books',views.books_view ),
    path('secret',views.secret ),
    path('get_all_images', views.getImages),

    path('books/<int:id>',views.books_view ),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('upload_image/',views.APIViews.as_view()),
    path('register',views.register ),
    path('addbook',views.add_book ),
]
