from django.conf.urls import url
from fiverrapp import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^gigs/(?P<id>[0-9]+)/$', views.gig_detail, name='gig_detail'),
    url(r'^create_gig/$', views.create_gig, name='create_gig'),
    url(r'^my_gigs/$', views.my_gigs, name='my_gigs'),
]
