from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})


def gig_detail(request, id):
    return render(request, 'gig_detail.html', {})
