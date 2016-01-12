from django.shortcuts import render
from .models import Item
from .forms import ItemForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone

# Create your views here.

def mainPage(request):
    return render(request, 'mainsite/mainPage.html', {})
def sellPage(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.vip = False;
            item.pub_date = timezone.now()
            item.save()
            # return redirect('mainsite/mainPage.html', pk=item.pk)
            return redirect('mainsite.views.item_detail', pk=item.pk)
            # return redirect('../')
    else:
        form = ItemForm()
    return render(request, 'mainsite/sellPage.html', {'form': form})
def buyPage(request):
    return render(request, 'mainsite/buyPage.html', {})
def estate(request):
    items = Item.objects.filter(category = "es").order_by('-pub_date') # pub_date__lte=timezone.now()
    return render(request, 'mainsite/category.html', {'items': items})
def transport(request):
    items = Item.objects.filter(category = "tr").order_by('-pub_date')
    return render(request, 'mainsite/category.html', {'items': items})
def electronics(request):
    items = Item.objects.filter(category = "el").order_by('-pub_date')
    return render(request, 'mainsite/category.html', {'items': items})
def stuff(request):
    items = Item.objects.filter(category = "st").order_by('-pub_date')
    return render(request, 'mainsite/category.html', {'items': items})
def services(request):
    items = Item.objects.filter(category = "ser").order_by('-pub_date')
    return render(request, 'mainsite/category.html', {'items': items})
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'mainsite/item.html', {'item': item})