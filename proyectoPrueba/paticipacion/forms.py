from django import forms

class RegistroEquipoForm(forms.Form):
    equipo = forms.CharField(
        label="Nombre del equipo",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre del equipo'})
    )

    # Lista desplegable desde Python
    JEFES = [
        ('', ''), 
        ('Condori Apaza Mariana Noemi C.I:12609475', 'Condori Apaza Mariana Noemi C.I:12609475'),
        ('Zamora Paredes Amilcar Brandon C.I:14793345', 'Zamora Paredes Amilcar Brandon C.I:14793345'),
        ('Duran Alipaz Deysi Beatriz C.I:13502101', 'Duran Alipaz Deysi Beatriz C.I:13502101'),
        ('Viscarra Arias Hernan C.I:4824889', 'Viscarra Arias Hernan C.I:4824889'),
        ('Soria Limachi Tito C.I:3475443', 'Soria Limachi Tito C.I:3475443'),
    ]

    jefe = forms.ChoiceField(
        label="Nombre del jefe",
        choices=JEFES,
        required=True,
    )

    # Campos adicionales
    membresia = forms.CharField(
        label="Membresía",
        max_length=100,
        required=True
    )

    cantidad = forms.IntegerField(
        label="Cantidad",
        min_value=1
    )
