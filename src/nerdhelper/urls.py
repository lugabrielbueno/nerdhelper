"""nerdhelper URL Configuration

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
from django.urls import path
from pages.views import home_view,settings_view
from calls.views import  formCalls
from categories.views import categories_list_view,categories_create_view,categories_update_view,categories_delete_view

urlpatterns = [
    path('', home_view, name='home'),
    # path('mycalls/detail', mycalls_detail_view, name='mycallsdetail'),
    # path('mycalls/list', mycalls_list_view, name='mycalls'),
    # path('calls/detail/<int:id>', calls_detail_view, name='callsdetail'),
    path('calls/create', formCalls, name='calls'),
    path('settings/list', settings_view, name='settings'),
    path('categories/list', categories_list_view, name='categories'),
    path('categories/create', categories_create_view, name='categoriescreate'),
    path('categories/<int:id>/update', categories_update_view, name='categoriesupdate'),
    path('categories/<int:id>/delete', categories_delete_view, name='categoriesdelete'),
    # path('categories/detail', categories_detail_view, name='categoriesdetail'),
    path('admin/', admin.site.urls)
]
