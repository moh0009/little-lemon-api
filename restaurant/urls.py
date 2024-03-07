from django.urls import path
from . import views
urlpatterns = [
    path('menu/', views.MenuAll.as_view()),
    path('menu/<int:pk>', views.MenuSingle.as_view()),
]
