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
from priorities.views import priorities_list_view,priorities_create_view,priorities_update_view,priorities_delete_view
from categories.views import categories_list_view,categories_create_view,categories_update_view,categories_delete_view
from status.views import status_list_view,status_create_view,status_update_view,status_delete_view
from calls.views import calls_list_view,calls_detail_view
from nerds.views import nerd_detail_view,nerd_list_view,nerd_create_view,nerd_delete_view

urlpatterns = [
    path('', home_view, name='home'),
    path('settings/list', settings_view, name='settings'),
    path('categories/list', categories_list_view, name='categories'),
    path('categories/create', categories_create_view, name='categoriescreate'),
    path('categories/<int:id>/update', categories_update_view, name='categoriesupdate'),
    path('categories/<int:id>/delete', categories_delete_view, name='categoriesdelete'),
    path('priorities/list', priorities_list_view, name='priorities'),
    path('priorities/create', priorities_create_view, name='prioritiescreate'),
    path('priorities/<int:id>/update', priorities_update_view, name='prioritiesupdate'),
    path('priorities/<int:id>/delete', priorities_delete_view, name='prioritiesdelete'),
    path('status/list', status_list_view, name='status'),
    path('status/create', status_create_view, name='statuscreate'),
    path('status/<int:id>/update', status_update_view, name='statusupdate'),
    path('status/<int:id>/delete', status_delete_view, name='statusdelete'),
    path('calls/list/', calls_list_view, name='calls'),
    path('calls/<int:id>/detail', calls_detail_view, name='callsdetail'),
    path('nerds/<int:id>/detail', nerd_detail_view, name='nerdsdetail'),
    path('nerds/list', nerd_list_view, name='nerds'),
    path('nerds/create', nerd_create_view, name='nerdscreate'),
    path('nerds/<int:id>/delete', nerd_delete_view, name='nerdsdelete'),
    path('admin/', admin.site.urls)
]
