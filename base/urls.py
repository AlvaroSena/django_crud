from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    path('api/v1/users', views.user_create),
    path('api/v1/users/all', views.user_list),
    path('api/v1/users/<str:username>', views.user_get),
    path('api/v1/users/update/password', views.user_password_update),
    path('api/v1/users/delete', views.user_delete)
]