from django.shortcuts import render, get_object_or_404
from .models import Mobile

def mobile_list(request):
    mobiles = Mobile.objects.all()
    return render(request, 'mobiles/mobile_list.html', {'mobiles': mobiles})

def mobile_detail(request, pk):
    mobile = get_object_or_404(Mobile, pk=pk)
    return render(request, 'mobiles/mobile_detail.html', {'mobile': mobile})
