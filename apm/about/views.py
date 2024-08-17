from django.shortcuts import render


def about(requets):
    return render(requets, 'about/about.html')
