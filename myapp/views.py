# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):

    context = {
        'message': 'Updating git part two'
    }

    return render(request, 'index.html', context)