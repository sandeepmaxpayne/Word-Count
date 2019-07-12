
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('counts/', views.count, name='count'),
    path('abouts/', views.about, name='about')
]
