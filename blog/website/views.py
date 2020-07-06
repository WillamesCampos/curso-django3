from django.shortcuts import render
from django.http import HttpResponse


def hello_blog(request):
    lista = [
        'Django', 'Python', 'Git', 'HTML',
        'Banco de Dados', 'wsgi'
    ]
    data = {
        "name": "Curso de Django 3", "lista_tecnologias": lista
    }
    return render(request, 'index.html', data)
