from django import forms
from django.forms import modelformset_factory, ModelForm
from .models import Assumptions

class AssumptionsForm(ModelForm):

    class Meta:
        model = Assumptions
        fields = ['Worst', 'Base', 'Best']
        exclude = ['Name']


