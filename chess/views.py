from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView
from django.template import Context, loader

def index(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template("chess.html")
    return HttpResponse(template.render())


class ChessView(TemplateView):
    template_name = 'home.html'

class HomeView(TemplateView):
    template_name = 'home.html'
