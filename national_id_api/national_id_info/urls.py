from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('national_id_info/<str:national_id>/', views.get_national_id_info_api, name='get_national_id_info'),
]
