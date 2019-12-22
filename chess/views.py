from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView

# Create your views here.
def index(request):
    return HttpResponse("hello world")

class ChessView(TemplateView):
    template_name = 'home.html'

class HomeView(TemplateView):
    template_name = 'home.html'
