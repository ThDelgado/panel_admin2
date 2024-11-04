from . import views
from django.urls import path, include
#importar clases de vista
from .views import LibrosView

urlpatterns = [
    path('newbook/', views.newbook, name= 'newbook'),
    path('libros/', LibrosView.as_view(), name= 'listbook'),
    path('add/modelform', views.add_libro_modelform, name="add_libro_modelform"),
]



