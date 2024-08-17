import requests
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import InscriptiontForm


def home(request):
    if request.method == "POST":
        form = InscriptiontForm(request.POST)
        if form.is_valid():
            """reCAPTCHA validation"""
            recaptcha_response = request.POST.get("g-recaptcha-response")
            data = {
                "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                "response": recaptcha_response,
            }
            r = requests.post(
                "https://www.google.com/recaptcha/api/siteverify", data=data
            )
            result = r.json()
            print(result)

            ''' if reCAPTCHA returns True '''
            if result['success']:
                print(result)
                print('FORMULARIO ENVIADO CON EXITO')
                cd = form.cleaned_data
                send_mail(
                    "Asunto: Inscripción",
                    "Nombre: {}\nCorreo electrónico: {}\nTeléfono contacto: {}\n"
                    "Política Privacidad :{}\nMensaje:\n\n{}".format(
                        cd["nombre"],
                        cd["email"],
                        cd["telefono"],
                        cd["politica_privacidad"],
                        cd["mensaje"],
                    ),
                    cd["email"],
                    ["to@example.com"],
                )

                return redirect('form_success')
                # return HttpResponseRedirect(reverse("inicio:gracias"))

    else:
        form = InscriptiontForm()

    return render(
        request,
        'core/home.html',
        {'form': form, "recaptcha_site_key": settings.GOOGLE_RECAPTCHA_SITE_KEY},
    )


def form_successfully(request):
    return render(request, 'core/thankyoupage.html')
