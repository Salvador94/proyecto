# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home (request):
    print request
    Titulo="medicamentos"
    return render(request, 'home.html', {'TitleV': Titulo})
