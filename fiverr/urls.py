from django.conf.urls import url, include
from django.contrib import admin
from fiverrapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^auth/', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('fiverrapp.urls'))
]
