from django.shortcuts import render
from .models import Coder

# Create your views here.
def coders_home(request):
    coders = Coder.objects.order_by('id')
    data = {
        'coders': coders,
    }
    return render(request, 'coders/home.html', data)

def coder_detail(request, id):
    data = {
        'coder_id': id,
    }
    return render(request, 'coders/coder_detail.html', data)
