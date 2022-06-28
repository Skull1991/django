from django.shortcuts import redirect, render


from item.models import item
from item.forms import ItemForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/user/login")
def index(request):
    items=item.objects.all()
    return render(request,"item/index.html",{'items':items})

@login_required(login_url="/user/login")
def create(request):
    return render(request,'item/create.html')

@login_required(login_url="/user/login")
def save(request):

    print(request.POST)
    print(request.FILES)
    data=ItemForm(request.POST,request.FILES)
    data.save()
    return redirect('/item')

@login_required(login_url="/user/login")
def edit(request,id):
    data=item.objects.get(id=id)
    print(id)
    return render(request,"item/edit.html",{'data':data})

@login_required(login_url="/user/login")
def update(request,id):
    data=item.objects.get(id=id)
    form=ItemForm(request.POST,request.FILES,instance=data)
    form.save()
    return redirect("/item")

@login_required(login_url="/user/login")
def delete(request,id):
    data=item.objects.get(id=id)
    data.delete()
    return redirect("/item")