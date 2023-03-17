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
