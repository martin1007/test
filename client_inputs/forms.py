from django import forms
from django.forms import modelformset_factory, ModelForm
from .models import Assumptions

class AssumptionsForm(ModelForm):

    class Meta:
        model = Assumptions
        fields = ['Worst_Case', 'Grey_Case', 'Red_Case', 'Blue_Case', 'Green_Case', 'Best_Case']
        exclude = ()


