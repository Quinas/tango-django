# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


def index(request):
    return HttpResponse('<a href="/rango/about/">About</a>')


def about(request):
    return HttpResponse('<a href="/rango/">Index</a>')
