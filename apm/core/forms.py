from django import forms


class InscriptiontForm(forms.Form):

    nombre = forms.CharField(max_length=100)
    telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "tel",
                "required": True,
                "pattern": "[0-9]{3}[0-9]{3}[0-9]{3}",
                "placeholder": "666555333",
                "class": "form-control border-black",
            }
        )
    )
    email = forms.EmailField()
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control border-black", "rows": "6"})
    )
    politica_privacidad = forms.BooleanField()

    nombre.widget.attrs.update({"class": "form-control border-black", "placeholder": "nombre"})
    email.widget.attrs.update({"class": "form-control border-black", "placeholder": "@correo"})
    politica_privacidad.widget.attrs.update(
        {"class": "form-check-label", "required": True}
    )
