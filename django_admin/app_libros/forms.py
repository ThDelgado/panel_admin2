from .models import Libros
from django import forms


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['titulo', 'autor', 'valoracion']
        # fields = "__all__" -> incluir todos los atributos del modelo
        # exclude = ['direccion'] -> no incluir los atributos que queremos
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),            
            'valoracion': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required', 'min': 0}),
        }
