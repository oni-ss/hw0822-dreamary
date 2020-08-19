from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.create, name="create"),
    path('introduce/', views.introduce, name="introduce"),
    path('update/<int:designer_id>/', views.update, name="update"),
]