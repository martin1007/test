from django.shortcuts import render
from .forms import  modelformset_factory, AssumptionsForm
from .models import Assumptions


def get_assumptions(request):

    if request.method == 'POST':

        if 'name' in request.POST:      
            
            formset = modelformset_factory(Assumptions, form = AssumptionsForm, extra = 5)

            if formset.is_valid():
                            
                print('valid form')            
            
                for form in formset:
                            
                    print('Looping forms')

                    assumptions =  form.save(commit='False')
                    assumptions.Name = 'name'
                    assumptions.save()
					


    else:

        formset = modelformset_factory(Assumptions, form = AssumptionsForm, extra = 5)    
	  

    return render(request, 'assumptions.html', {'formset': formset})

