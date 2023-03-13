from django.shortcuts import render
from .models import Banner, TeamMember
from coders.models import Coder

# Create your views here.
def home(request):
    banners = Banner.objects.all
    team_members = TeamMember.objects.all
    featured_coders = Coder.objects.filter(is_featured=True)
    new_coders = Coder.objects.order_by('-created_date')[:5]

    data = {
        "banners": banners,
        "team": team_members,
        'featured_coders': featured_coders,
        'new_coders': new_coders,
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    return render(request, 'webpages/about.html')

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')