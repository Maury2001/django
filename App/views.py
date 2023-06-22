from django.shortcuts import render, get_object_or_404
from App.models import Flower
# Create your views here.

def index(request):

    flowers = Flower.objects.all()

    return render(request, 'App/index.html', {'flowers':  flowers})

def detail(request, id=None):
    flower = get_object_or_404(Flower, id=id)

    return render(request, 'App/detail.html', {'flower': flower})