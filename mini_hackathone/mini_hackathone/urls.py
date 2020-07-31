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
from django.conf import settings
from django.conf.urls.static import static
from dongnaechekbang import views
import dongnaechekbang.views

app_name = 'dongnaechekbang'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dongnaechekbang.views.home, name='home'),
    path('search/',dongnaechekbang.views.search, name='search'),
    path('location/', views.location, name="location"),
    path('community',dongnaechekbang.views.community.as_view(), name='community'),
    path('community_view<pk>',dongnaechekbang.views.community_view.as_view(),name="community_view"),
    path('community_delete/<pk>',dongnaechekbang.views.community_delete.as_view(),name="community_delete"),
    path('community_update/<pk>',dongnaechekbang.views.community_update.as_view(),name="community_update"),
    path('community_write',dongnaechekbang.views.community_write.as_view(),name='community_write'),
    path('comment_write/<int:pk>',dongnaechekbang.views.comment_write,name='comment_write'),
    path('location/<int:bookstore_id>', views.location_bookstore, name="bookstore"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
