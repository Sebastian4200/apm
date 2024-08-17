from django import forms


class ContactForm(forms.Form):

    nombre = forms.CharField(max_length=100)
    asunto = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control border-black", "rows": "6"})
    )
    politica_privacidad = forms.BooleanField()

    nombre.widget.attrs.update(
        {"class": "form-control border-black", "placeholder": "nombre"}
    )
    asunto.widget.attrs.update(
        {"class": "form-control border-black", "placeholder": "asunto"}
    )
    email.widget.attrs.update(
        {"class": "form-control border-black", "placeholder": "@correo"}
    )
    politica_privacidad.widget.attrs.update(
        {"class": "form-check-label", "required": True}
    )
