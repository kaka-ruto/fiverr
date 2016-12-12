from django.forms import ModelForm
from .models import Gig

class GigForm(ModelForm):
    class Meta:
        model = Gig
        fields = ['title', 'category', 'description', 'price', 'photo', 'status']
