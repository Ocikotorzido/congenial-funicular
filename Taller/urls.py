"""Taller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from Mantenedor.views import to_index

# from django.conf.urls import url
# from django.contrib.auth import login
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Mantenedor/', include('Mantenedor.urls'), name='Mantenedor'),
    path('', to_index, name='to_index'), # Redirecciona hacia "/Mantenedor/index".

    # url(r'^$', login, {'template_name': 'login.html'}, name='login'),
    # path('accounts/', include('django.contrib.auth.urls')),
]




















