"""
URL configuration for project_toko project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app_toko.views import home, kategori ,del_kategori, add_kategori, edit_kategori, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('kategori', kategori, name='kategori'),
    path('kategori/del/<int:k_id>', del_kategori, name='del_kategori'),
    path('kategori/form', add_kategori, name='add_kategori'),
    path('kategori/edit/<int:k_id>', edit_kategori, name='edit_kategori'),
    path('login/', login, name='login'),
]
