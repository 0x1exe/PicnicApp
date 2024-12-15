
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from .models import Item

def landing_page(request):
    return render(request, 'store/landing_page.html')

def catalog_page(request):
    query = request.GET.get('q')
    if query:
        items = Item.objects.filter( Q(name__icontains = query) | Q(description__icontains = query) | Q(image_description__icontains = query))
    else:
        items = Item.objects.all()
    return render(request, 'catalog.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_detail.html', {'item': item})

def download_page(request):
    return render(request, 'store/download_page.html')

