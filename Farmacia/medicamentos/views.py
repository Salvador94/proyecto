# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import medicamento

# Create your views here.

def home (request):
    print request
    Titulo="medicamentos"
    return render(request, 'home.html', {'TitleV': Titulo})

#def lista_medicamentos(request):
    #result_set = medicamento.object.all()
    #context = {
    #"result": result_set
    #}
    #return render(request, "lista_medicamentos.html", context)

def detalle_medicamento(request, id=1):
    result_set = medicamento.objects.get(id=id)
    context = {
    "result": result_set
    }
    return render(request, "detalle_medicamento.html", context)
