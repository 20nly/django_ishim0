from django.urls import path
from . import views



urlpatterns = [
    path('', views.board, name="board"),
    path('resume/<str:pk>/', views.resume, name="resume"),
    path('vacancy/<str:pk>/', views.vacancy, name="vacancy"),
]