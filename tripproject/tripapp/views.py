from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, TeamMember


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    return render(request, "index.html", {'result': obj})

def team_view(request):
    team_members = TeamMember.objects.all()
    return render(request, "index.html", {'team_members': team_members})
