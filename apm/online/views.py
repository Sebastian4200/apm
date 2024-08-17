from django.shortcuts import render


def online_classes(request):
    return render(request, 'online/online-classes.html')
