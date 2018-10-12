# -*- coding: utf-8 -*-
from django.shortcuts import render

def quadratic_results(request):
    print request.GET
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    aa, bb, cc = None, None, None
    x1, x2 = None, None
    res_err = None
    if not b:
        bb = u"коэффциент не определен"
        
    if not c:
        cc = u"коэффциент не определен"

    if not a:
        aa = u"коэффциент не определен"

    if b.isdigit():
        b = int(b)
    elif not bb:
        if b.startswith("-") and b[1:].isdigit():
            b = - int(b[1:])
        else:            
            bb = u"Не целое число"

    if c.isdigit():
        c = int(c)
    elif not cc:
        if c.startswith("-") and c[1:].isdigit():
            c = - int(c[1:])
        else:            
            cc = u"Не целое число"

    if a.isdigit():
        a = int(a)
    elif not aa:
        if a.startswith("-") and a[1:].isdigit():
            a = - int(a[1:])
        else:            
            aa = u"Не целое число"
    if a == 0:
        aa = u"коэффициент при первом слогаемом уравнения не может быть = 0"
    if not aa and not bb and not cc:
        D = b**2 - 4*a*c
        if D > 0:
            x1 = (-b + pow(D, 0.5)) / (2*a)
            x2 = (-b - pow(D, 0.5)) / (2*a) 
        else:
            res_err = u"Дискриминант меньше 0!"
    print a, b , c, x1, x2
    context = {'a':a, 'b':b, 'c':c, 'a_err': aa, 'b_err': bb, 'c_err': cc, 'x1': x1, 'x2': x2, 'res_err': res_err }
    return render(request, "results.html", context)


