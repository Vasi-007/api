from django.shortcuts import render,redirect,get_object_or_404
from .models import Gadjet
import requests

# Create your views here.

def gadjet_list(request):
  gadjets = Gadjet.objects.all()
  return render(request,"gadjetapp/gadjet_list.html",{"gadjets":gadjets})


def gadjet_create(request):
  if request.method == "POST":
    Gadjet.objects.create(
      title = request.POST["title"],
      brand = request.POST["brand"],
      price = request.POST["price"],
      warranty_years = request.POST["warranty_years"],
    )
    return redirect("gadjet_list")
  return render(request,"gadjetapp/gadjet_create.html")


def gadjet_update(request,id):
  gadjet = get_object_or_404(Gadjet,id=id)
  if request.method == "POST":
    gadjet.title = request.POST["title"]
    gadjet.brand = request.POST["brand"]
    gadjet.price = request.POST["price"]
    gadjet.warranty_years= request.POST["warranty_years"]
    gadjet.save()
    return redirect("gadjet_list")
  
  return redirect(request,"gadjetapp/gadjet_update.html",{"gadjet":gadjet})


def gadjet_delete(request,id):
  gadjet = get_object_or_404(Gadjet,id=id)
  if request.method == "POST":
    gadjet.delete()
    return redirect("gadjet_list")
  return render(request,"gadjetapp/gadjet_delete.html",{gadjet:gadjet})
  



