from django.shortcuts import render, get_object_or_404
from .models import Coder

# Create your views here.
def coders_home(request):
    coders = Coder.objects.order_by('id')
    data = {
        'coders': coders,
    }
    return render(request, 'coders/home.html', data)

def coder_detail(request, id):
    coder = get_object_or_404(Coder, pk=id)

    data = {
        'coder': coder,
    }
    return render(request, 'coders/coder_detail.html', data)

def search(request):
    coders = Coder.objects.order_by('id')
    cities = Coder.objects.values_list('city', flat=True).distinct()
    types = Coder.objects.values_list('type', flat=True).distinct()
    categories = Coder.objects.values_list('category', flat=True).distinct()


    if 'keyword' in request.GET:
        key_value = request.GET['keyword']
        if key_value:
            coders = coders.filter(category__icontains=key_value)

    
    if 'city' in request.GET:
        key_value = request.GET['city']
        if key_value:
            coders = coders.filter(city__iexact=key_value)

    
    if 'type' in request.GET:
        key_value = request.GET['type']
        if key_value:
            coders = coders.filter(type__iexact=key_value)

    if 'category' in request.GET:
        key_value = request.GET['category']
        if key_value:
            coders = coders.filter(category__iexact=key_value)

    data = {
        'coders': coders,
        'cities': cities,
        'types': types,
        'categories': categories,
    }
    return render(request, 'coders/search.html', data)
