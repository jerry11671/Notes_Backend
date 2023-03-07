from django.urls import path, include
from . import views

urlpatterns = [
    path('notes/', views.getNote),
    path('notes/create/', views.createNote),
    path('notes/update/<str:pk>/', views.updateNote),
    path('notes/delete/<str:pk>/', views.deleteNote),
    path('notes/<str:pk>/', views.viewNote),
]


    