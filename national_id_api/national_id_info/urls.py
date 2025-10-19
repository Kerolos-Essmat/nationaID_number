from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('national_id_info/<str:national_id>/', views.get_national_id_info_api, name='get_national_id_info'),
    path('token/', obtain_auth_token, name='api-token'),
]
