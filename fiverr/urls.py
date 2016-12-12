from django.conf.urls import url, include
from django.contrib import admin
# To serve static files during development
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^auth/', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('fiverrapp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
