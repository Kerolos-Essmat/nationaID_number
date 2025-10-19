from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('national_id_info/', views.get_national_id_info, name='get_national_id_info'),
]
