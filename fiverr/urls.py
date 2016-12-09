from django.conf.urls import url
from django.contrib import admin
from fiverrapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^gigs/(?P<id>[0-9]+)/$', views.gig_detail, name='gig_detail'),
]
