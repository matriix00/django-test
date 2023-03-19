from django.shortcuts import render,redirect
from food.forms import FoodForm

from food.models import Food

from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.
def foodIndex(request):
    allfood= [
        {"id":1,"name":"fish","image":"fish.jpeg"},
        {"id":2,"name":"kofta","image":"kofta.jpeg"},
        {"id":3,"name":"koushary","image":"koushry.jpeg"},
        {"id":4,"name":"mahshi","image":"mahshi.jpeg"},
        {"id":5,"name":"melokhia","image":"melo.jpeg"},
        
    ]
    return render(request,"food/allfood.html",{"allfood":allfood})


def findex(request):
    food=Food.objects.all()
    return render(request,"food/index.html",{"food":food})


def show(request,id):
    item=Food.objects.get(pk=id)
    return render(request,"food/show.html",{"item":item})

def delete(request,id):
    food = Food.objects.get(pk=id)
    food.delete()
    return redirect("/myfood/foodhome")


class CreateFoodView(CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'food/create.html'
    success_url = '/myfood/foodhome'
#2
class UpdateFoodView(UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'food/create.html'
    success_url = '/myfood/foodhome'

