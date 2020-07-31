"""mini_hackathone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import dongnaechekbang.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dongnaechekbang.views.home, name='home'),
    path('location/',dongnaechekbang.views.location, name='location'),
    path('search/',dongnaechekbang.views.search, name='search'),
    path('community',dongnaechekbang.views.community.as_view(), name='community'),
    # path('community_delete',dongnaechekbang.views.community_delete,name='community_delete'),
    # path('community_reply',dongnaechekbang.views.community_reply,name='community_delete_reply'),
    # path('community_update',dongnaechekbang.views.community_update,name='community_update'),
    # path('community/<int:blog_id>',dongnaechekbang.views.community_view,name='community_view'),
    # path('community_write',dongnaechekbang.views.community_write,name='community_write'),
    path('community_view<pk>',dongnaechekbang.views.community_view.as_view(),name="community_view"),
    path('community_delete/<pk>',dongnaechekbang.views.community_delete.as_view(),name="community_delete"),
    path('community_update/<pk>',dongnaechekbang.views.community_update.as_view(),name="community_update"),
    path('community_write',dongnaechekbang.views.community_write.as_view(),name='community_write'),
    path('comment_write/<int:pk>',dongnaechekbang.views.comment_write,name='comment_write'),

]


