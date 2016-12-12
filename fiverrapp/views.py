from django.shortcuts import render, redirect
from .models import Gig

def home(request):
    gigs = Gig.objects.filter(status=True)
    return render(request, 'home.html', {"gigs": gigs})


def gig_detail(request, id):
    try:
        gig = Gig.objects.get(id=id)
    except Gig.DoesNotExist:
        return redirect('/')
    return render(request, 'gig_detail.html', {"gig": gig})
