from django.urls import path
from . import views

app_name = 'mobiles'

urlpatterns = [
    path('', views.mobile_list, name='list'),
    path('<int:pk>/', views.mobile_detail, name='detail'),
]
