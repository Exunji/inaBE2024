from django.shortcuts import render

from django.http import HttpResponse

def index2(request):
    return HttpResponse("<h1>soy index app2<h1>")

def despacito(request):
    html="""<a href="/app2/index">volver</a>
    <img src="https://static.wikia.nocookie.net/albertsstuffs/images/9/93/Despacitospider.jpg/revision/latest?cb=20200923201313" alt="despacito">"""
    return HttpResponse(html)
