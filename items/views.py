from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def home(request):
    if request.method == "POST":
        form = ItemForms(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect("home")        
        else:
            pass
        
    else:
        form = ItemForms()
        
    items = Item.objects.filter(user=request.user)
    
    return render(
                request, "home.html",
                {
            "items": items,
            "form": form,
        }
                
    )
    
    
@login_required
def update(request, id):
    item = Item.objects.get(id=id, user=request.user)
    if request.method == "POST":
        form = ItemForms(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect("home")        
        else:
            pass
        
    else:
        form = ItemForms(instance=item)
        
    return render(
        request,
        "update.html",
        {
            "item": item,
            "form": form,
        }
    )  
        

@login_required
def delete(request, id):
    if request.method == "POST":    
        delete = Item.objects.get(id=id ,user=request.user )
        delete.delete()
        return redirect("home")
    

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        
    else:
        form = UserCreationForm()
        
    return render(
        request, "register.html",
        {
            "form": form,
        }
    )
        