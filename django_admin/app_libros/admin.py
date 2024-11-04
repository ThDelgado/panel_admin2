
from django.contrib import admin
from .models import Libros

# Register your models here.


@admin.register(Libros)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor','valoracion']
    search_fields = ['titulo', 'autor', 'valoracion' ] #filtro 
    ordering = ['titulo']
