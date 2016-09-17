# -*- coding: utf-8 -*-
from django.http import *

def merhaba_django(request):
    return HttpResponse(u'Merhaba Django')