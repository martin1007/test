from django.shortcuts import render
from .forms import  modelformset_factory, AssumptionsForm
from .models import Revenue_Assumptions, COGS_Assumptions, Assumptions

model_names = [Revenue_Assumptions, COGS_Assumptions]


def get_assumptions(request):

    AssumptionsFormSet_dict = {}

    for name in model_names:
        modelformset_ = modelformset_factory(name, form = AssumptionsForm, extra = 5)
        AssumptionsFormSet_dict[str(name)] = modelformset_

    if request.method == 'POST' and str(name) in request.POST:

        formset = AssumptionsFormSet_dict[str(name)]
        
        if formset.is_valid():
                       
            print('valid form')
            print(str(name))
            
            for form in formset:
                            
                print('in for loop after valid form1')

                name =  form.save()

                          
    else:
	
	    
	    for key, value in AssumptionsFormSet_dict.items():	
	        
                
	        formset = AssumptionsFormSet_dict[key]

	        print('reached else')
		        
       

    return render(request, 'assumptions.html', {'formset': formset, 'model_names': model_names, 'name' : name})

