from django.shortcuts import render, get_object_or_404
from App.models import Flower
from django.http import HttpResponseRedirect
from App.forms import MyForm
# Create your views here.


def index(request):

    q = request.GET.get('q', None)
    items = ''
    if q is None or q is "":
        flowers = Flower.objects.all()

    elif q is not None:
        flowers = Flower.objects.filter(title__contains=q)

    return render(request, 'App/index.html', {'flowers':  flowers})


def detail(request, id=None):
    flower = get_object_or_404(Flower, id=id)

    return render(request, 'App/detail.html', {'flower': flower})


def create(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = MyForm()

    return render(request, 'App/edit.html', {'form': form})

def edit(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method =='POST':
        form = MyForm(request.POST, instance=flower)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        
    else:
        form = MyForm(instance=flower)

    return render(request, 'App/edit.html', {'form':form})

def delete(request, pk = None):
    flower = get_object_or_404(Flower, pk=pk)
    flower.delete()

    return render (request, 'App/index.html')