from django.shortcuts import render, redirect
from .models import Libros
from django.http import HttpResponse
from .forms import LibroForm
from django.forms import ValidationError
from django.contrib import messages

#filtros 
from django.views.generic import ListView 
from django.utils import timezone
from datetime import timedelta, datetime



# Create your views here.

def newbook(request):
    return render(request,"books/newbook.html", {})

class LibrosView(ListView):
    model = Libros
    template_name = "books/listbook.html"
    context_object_name = "libros"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Pagina de libros"
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        valoracion  = self.request.GET.get("valoracion", None)
        filtro_fecha = self.request.GET.get("filtro_fecha", None)

        
        #filtrado valoracion
        if valoracion:
            valoraciones_permitidas = [ 750, 1350, 1570, 2100, 2540, 3250]
            if int(valoracion) in valoraciones_permitidas:
                queryset = queryset.filter(valoracion = valoracion)
                
        #filtrado por fecha
        today = timezone.now().date()
        if filtro_fecha == "hoy":
            queryset = queryset.filter(fecha_modificacion__gte=today)
        elif filtro_fecha == "ultimos_7_dias":
            queryset = queryset.filter(fecha_modificacion__gte=today - timedelta(days=7))
            
        elif filtro_fecha == "ultimo_mes":
            queryset = queryset.filter(fecha_modificacion__gte=today - timedelta(days=30))
        elif filtro_fecha == "ultimo_anno":
            queryset = queryset.filter(fecha_modificacion__gte=today - timedelta(days=365))
        elif filtro_fecha == "cualquier_fecha":
            queryset = queryset.filter(fecha_modificacion__gte=today - timedelta(days=0)) 
        
        return queryset

                   
def add_libro_modelform(request):

    if request.method == 'GET':
        form = LibroForm()
        contexto = {'form': form}
        return render(request, "books/add_libro_modelform.html", contexto)
    
    

        #logica para procesar los datos.
    if request.method == 'POST':
        form = LibroForm(request.POST)
        

        if form.is_valid():
            try:  
                libro = form.save(commit=False)
                libro.clean()         
                libro.save()
                messages.success(request, "Libro creado correctamente")
                return redirect('listbook')
            except ValidationError as e:
                messages.error(request, e.messages )

        else:
            
            messages.error(request, "Error al intentar crear el producto, intente nuevamente")
            return render(request, "books/add_libro_modelform.html", {"form": LibroForm()})
            
      
    contexto = {"form": form}
    return render(request, "books/add_libro_modelform.html", contexto)