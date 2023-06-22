from django.shortcuts import render
from App.models import Flower
# Create your views here.

def index(request):

    flowers = Flower.objects.all()

    return render(request, 'App/index.html', {'flowers': flowers})
