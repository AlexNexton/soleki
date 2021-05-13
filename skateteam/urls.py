from django.urls import path
from . import views

urlpatterns = [
    path('', views.skateteam, name='skateteam'),
    path('<int:memeber_id>/', views.sdetail, name='sdetail'),
]
