from django.urls import path
from . import views
urlpatterns = [
    path('menu/', views.MenuAll.as_view(),name = "menu"),
    path('menu/<int:pk>', views.MenuSingle.as_view()),
]
