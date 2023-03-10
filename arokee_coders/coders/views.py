from django.shortcuts import render

# Create your views here.
def coders_home(request):
    return render(request, 'coders/home.html')