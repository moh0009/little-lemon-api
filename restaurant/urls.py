from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("index/", views.index),
    path('menu/', views.MenuAll.as_view(),name = "menu"),
    path('menu/<int:pk>', views.MenuSingle.as_view()),
    path('api-token-auth/', obtain_auth_token),
]
