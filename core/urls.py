from django.urls import path
from . import views

urlpatterns = [
    path('vagas/',        views.vaga_list,   name='vaga_list'),
    path('vagas/nova/',   views.vaga_create, name='vaga_create'),
    path('vagas/<int:pk>/editar/', views.vaga_edit,   name='vaga_edit'),
    path('dashboard/',    views.dashboard,   name='dashboard'),
]
