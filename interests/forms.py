from django.forms import ModelForm
from interests.models import Interest


class InterestForm(ModelForm):
    class Meta:
        model = Interest
        fields = ['email', 'first_name', 'last_name']
