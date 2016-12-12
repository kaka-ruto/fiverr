from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Gig
from .forms import GigForm


def home(request):
    gigs = Gig.objects.filter(status=True)
    return render(request, 'home.html', {"gigs": gigs})


def gig_detail(request, id):
    try:
        gig = Gig.objects.get(id=id)
    except Gig.DoesNotExist:
        return redirect('/')
    return render(request, 'gig_detail.html', {"gig": gig})

@login_required(login_url="/")
def create_gig(request):
    if request.method == 'POST':
        gig_form = GigForm(request.POST, request.FILES)
        print(gig_form.is_valid())
        print(gig_form.errors())

    gig_form = GigForm()
    return render(request, 'create_gig.html', {"gig_form": gig_form})

@login_required(login_url="/")
def my_gigs(request):
    gigs = Gig.objects.filter(user=request.user)
    return render(request, 'my_gigs.html', {"gigs": gigs})
