from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(label="nombre", required=True,  help_text="Escriba su nombre tal como figura en su documento.")
    correo = forms.EmailField(label="correo", required=True)
    edad = forms.IntegerField(label="edad", required=True)

