from django.urls import path, include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    TableRestoListApiView,TableRestoDetailApiView,RegisterUserAPIView,LoginView,MenuRestoView
)
app_name = 'api'

urlpatterns = [
    #path('api/v1/login', LoginView.as_view()),
    #path('api/v1/logout', LogoutView.as_view()),
    #path('api/v1/register', RegisterWaitressAPI.as_view()),
    path('api/table_resto', TableRestoListApiView.as_view()),
    path('api/table_resto/<int:id>', TableRestoDetailApiView.as_view()),
    path('api/register', views.RegisterUserAPIView.as_view()),
    path('api/login', views.LoginView.as_view()),
    path('api/menu-resto', MenuRestoView.as_view()),
    path('api/menu-resto-filter', views.MenuRestoFilterApi.as_view()),
    path('api/menu-resto-filter/', views.MenuRestoFilterApi.as_view(), name='menu-resto-filter'),
]