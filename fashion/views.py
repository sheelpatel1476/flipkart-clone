from django.shortcuts import render, get_object_or_404
from .models import FashionItem

def fashion_list(request):
    items = FashionItem.objects.all()
    return render(request, 'fashion/fashion_list.html', {'items': items})

def fashion_detail(request, pk):
    item = get_object_or_404(FashionItem, pk=pk)
    return render(request, 'fashion/fashion_detail.html', {'item': item})
