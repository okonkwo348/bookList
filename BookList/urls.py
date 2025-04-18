"""
URL configuration for BookList project.

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
from django.urls import path, include
from BookListAPI.views import user_info 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('BookListAPI.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration', include('dj_rest_auth.registration.urls')),
    path('accounts/',include('allauth.urls')),
    path('/api/user-info/', user_info, name='user_info'),
    path('_debug_/',include('debug_toolbar.urls')),
]
