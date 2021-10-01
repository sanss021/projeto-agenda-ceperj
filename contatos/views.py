from django.shortcuts import render

import contatos
from .models import Contato

def index(request):
    contatos = Contato.objects.all()
    return render (request, 'contatos/index.html', {
        'contatos': contatos
    })
