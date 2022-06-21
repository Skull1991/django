from django.shortcuts import redirect, render


from item.models import item
from item.forms import ItemForm
# Create your views here.
def index(request):
    items=item.objects.all()
    return render(request,"item/index.html",{'items':items})

def create(request):
    return render(request,'item/create.html')

def save(request):
    print(request.POST)
    data=ItemForm(request.POST)
    data.save()

    return redirect('/item')