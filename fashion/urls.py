from django.urls import path
from . import views

app_name = 'fashion'

urlpatterns = [
    path('', views.fashion_list, name='list'),
    path('<int:pk>/', views.fashion_detail, name='detail'),
]
