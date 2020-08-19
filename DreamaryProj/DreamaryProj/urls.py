from django.contrib import admin
from django.urls import path, include
from DreamaryApp import views
import DreamaryApp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('DreamaryApp/', include(DreamaryApp.urls)),
]