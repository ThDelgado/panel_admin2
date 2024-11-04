from django.db import models
from django.forms import ValidationError
from django.utils import timezone
# Create your models here.
class Libros(models.Model):
    

    titulo = models.CharField(max_length=200,blank=False, null=False)
    autor = models.CharField(max_length=150, blank=False, null=False)
    valoracion = models.IntegerField(default=0, blank=False, null=False)
    fecha_modificacion = models.DateField(default=timezone.now,blank=False, null=False )

    def clean(self):
        #validar el campo valoracion
        if not (0 < self.valoracion < 1000):
            raise ValidationError({"valoracion": "La valoracion debe ser mayor que 0 y menor que 10,000"})
    
    def __str__(self):
        return self.titulo
    
    class Meta:
	    permissions = [('development', 'Desarrolladorls')]

