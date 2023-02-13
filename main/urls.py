from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('custody-list/', views.cus_list, name='cus-list'),
    path('request-list/', views.req_list, name='req-list'),
]