from django.contrib import admin

from .models import Historical_Income_Statement, Historical_Balance_Sheet, Historical_Cash_Flow_Statement, Assumptions

admin.site.register(Assumptions)
admin.site.register(Historical_Income_Statement)
admin.site.register(Historical_Balance_Sheet)
admin.site.register(Historical_Cash_Flow_Statement)


