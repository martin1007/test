from django.db import models
from django.forms import ModelForm

class Historical_Income_Statement(models.Model):

    Historical_Dates = models.CharField(max_length=30)
    
    Revenue = models.FloatField(null=True, blank=True, default=None)
    COGS = models.FloatField(null=True, blank=True, default=None)
    
    Gross_Margin = models.FloatField(null=True, blank=True, default=None)
    Selling_Marketing = models.FloatField(null=True, blank=True, default=None)
    Research_Development = models.FloatField(null=True, blank=True, default=None)
    General_Administrative = models.FloatField(null=True, blank=True, default=None)
    #Other_Operating_Expense = models.FloatField(null=True, blank=True, default=None)
    Total_Operating_Expense = models.FloatField(null=True, blank=True, default=None)
    EBITDA = models.FloatField(null=True, blank=True, default=None)
    Depreciation = models.FloatField(null=True, blank=True, default=None)
    Goodwill_Impairment = models.FloatField(null=True, blank=True, default=None)
    Amortization = models.FloatField(null=True, blank=True, default=None)
    Allowance_for_Doubtful_Accounts = models.FloatField(null=True, blank=True, default=None)
    Inventory_Reserve = models.FloatField(null=True, blank=True, default=None)
    #Other_Expense = models.FloatField(null=True, blank=True, default=None)
    EBIT = models.FloatField(null=True, blank=True, default=None)
    Interest_Expense = models.FloatField(null=True, blank=True, default=None)
    Interest_Income = models.FloatField(null=True, blank=True, default=None)
    Income_before_Income_Taxes = models.FloatField(null=True, blank=True, default=None)
    
    Current_Income_Tax = models.FloatField(null=True, blank=True, default=None)
    Deferred_Income_Tax = models.FloatField(null=True, blank=True, default=None)
    Total_Income_Tax_Provision = models.FloatField(null=True, blank=True, default=None)
    Net_Income = models.FloatField(null=True, blank=True, default=None)

class Historical_Balance_Sheet(models.Model):
    
    Historical_Dates = models.CharField(max_length=30)
    
    
    Cash = models.FloatField(null=True, blank=True, default=None)
    Marketable_Securities = models.FloatField(null=True, blank=True, default=None)
    Accounts_Receivables = models.FloatField(null=True, blank=True, default=None)
    Allowance_for_Doubtful_Accounts = models.FloatField(null=True, blank=True, default=None)
    Net_Accounts_Receivables = models.FloatField(null=True, blank=True, default=None)
    Inventories = models.FloatField(null=True, blank=True, default=None)
    Inventory_Reserves = models.FloatField(null=True, blank=True, default=None)
    Net_Inventories = models.FloatField(null=True, blank=True, default=None)
    Prepaid_Assets = models.FloatField(null=True, blank=True, default=None)
    Other_Current_Assets = models.FloatField(null=True, blank=True, default=None)
    Total_Current_Assets = models.FloatField(null=True, blank=True, default=None)
    
    Property_Plant_Equipment = models.FloatField(null=True, blank=True, default=None)
    Accumulated_Depreciation = models.FloatField(null=True, blank=True, default=None)
    Net_PPE = models.FloatField(null=True, blank=True, default=None)
    Goodwill = models.FloatField(null=True, blank=True, default=None)
    Impairment = models.FloatField(null=True, blank=True, default=None)
    Net_Goodwill = models.FloatField(null=True, blank=True, default=None)
    Intellectual_Property = models.FloatField(null=True, blank=True, default=None)
    Accumulated_Amortization = models.FloatField(null=True, blank=True, default=None)
    Net_IP = models.FloatField(null=True, blank=True, default=None)
    Net_Long_Term_Assets = models.FloatField(null=True, blank=True, default=None)
    Total_Assets = models.FloatField(null=True, blank=True, default=None)
    
    
    Accounts_Payables = models.FloatField(null=True, blank=True, default=None)
    Accrued_Liabilities = models.FloatField(null=True, blank=True, default=None)
    Revolver = models.FloatField(null=True, blank=True, default=None)
    Income_Taxes_Payable = models.FloatField(null=True, blank=True, default=None)
    Current_Portion_of_Deferred_Tax_Liabilities = models.FloatField(null=True, blank=True, default=None)
    Other_Current_Liabilities = models.FloatField(null=True, blank=True, default=None)
    Current_Portion_of_Long_Term_Funded_Debt = models.FloatField(null=True, blank=True, default=None)
    Current_Portion_of_Capitalized_Leases = models.FloatField(null=True, blank=True, default=None)
    Other_Rounding_Difference = models.FloatField(null=True, blank=True, default=None)
    Common_Dividend_Payable = models.FloatField(null=True, blank=True, default=None)
    Preferred_Dividend_Payable = models.FloatField(null=True, blank=True, default=None)
    Total_Current_Liabilities = models.FloatField(null=True, blank=True, default=None)
    
    Long_Term_Funded_Debt = models.FloatField(null=True, blank=True, default=None)
    Long_Term_Capital_Leases = models.FloatField(null=True, blank=True, default=None)
    Deferred_Tax_Liability_Long_Term = models.FloatField(null=True, blank=True, default=None)
    Other_Long_Term_Debt = models.FloatField(null=True, blank=True, default=None)
    Total_Long_Term_Debt = models.FloatField(null=True, blank=True, default=None)
    Total_Liabilities = models.FloatField(null=True, blank=True, default=None)
    
    Common_Stock_at_par = models.FloatField(null=True, blank=True, default=None)
    Preferred_Stock_at_par = models.FloatField(null=True, blank=True, default=None)
    Paid_in_Capital_Common_Stock = models.FloatField(null=True, blank=True, default=None)
    Paid_in_Capital_Preferred_Stock = models.FloatField(null=True, blank=True, default=None)
    Current_Period_Net_Income = models.FloatField(null=True, blank=True, default=None)
    Retained_Earnings = models.FloatField(null=True, blank=True, default=None)
    Common_Dividend = models.FloatField(null=True, blank=True, default=None)
    Preferred_Dividend = models.FloatField(null=True, blank=True, default=None)
    Total_Equity = models.FloatField(null=True, blank=True, default=None)
    Total_Liabilities_and_Equity = models.FloatField(null=True, blank=True, default=None)

class Historical_Cash_Flow_Statement(models.Model):
    
    Historical_Dates = models.CharField(max_length=30)
    
    Net_Income = models.FloatField(null=True, blank=True, default=None)
    Depreciation = models.FloatField(null=True, blank=True, default=None)
    Goodwill_Impairment = models.FloatField(null=True, blank=True, default=None)
    Amortization = models.FloatField(null=True, blank=True, default=None)
    Change_in_Allowance_for_Doubtful_Accounts = models.FloatField(null=True, blank=True, default=None)
    Change_in_Inventory_Reserve = models.FloatField(null=True, blank=True, default=None)
    Cash_from_Operations = models.FloatField(null=True, blank=True, default=None)
    
    Marketable_Securities = models.FloatField(null=True, blank=True, default=None)
    Accounts_Receivables = models.FloatField(null=True, blank=True, default=None)
    Inventories = models.FloatField(null=True, blank=True, default=None)
    Prepaid_Assets = models.FloatField(null=True, blank=True, default=None)
    Other_Current_Assets = models.FloatField(null=True, blank=True, default=None)
    Accounts_Payables = models.FloatField(null=True, blank=True, default=None)
    Accrued_Liabilities = models.FloatField(null=True, blank=True, default=None)
    Revolver = models.FloatField(null=True, blank=True, default=None)
    Income_Taxes_Payable = models.FloatField(null=True, blank=True, default=None)
    Current_Portion_of_Deferred_Tax_Liabilities = models.FloatField(null=True, blank=True, default=None)
    Other_Current_Liabilities = models.FloatField(null=True, blank=True, default=None)
    Current_Portion_of_Long_Term_Funded_Debt = models.FloatField(null=True, blank=True, default=None)
    Current_Portion_of_Capitalized_Leases = models.FloatField(null=True, blank=True, default=None)
    Other_Rounding_Difference = models.FloatField(null=True, blank=True, default=None)
    Common_Dividend_Payable = models.FloatField(null=True, blank=True, default=None)
    Preferred_Dividend_Payable = models.FloatField(null=True, blank=True, default=None)
    Cash_from_Working_Capital = models.FloatField(null=True, blank=True, default=None)
    
    Capital_Expenditures = models.FloatField(null=True, blank=True, default=None)
    Goodwill = models.FloatField(null=True, blank=True, default=None)
    Intangible_Assets = models.FloatField(null=True, blank=True, default=None)
    Cash_from_Investing_Activities = models.FloatField(null=True, blank=True, default=None)
    
    Long_Term_Funded_Debt = models.FloatField(null=True, blank=True, default=None)
    Long_Term_Capital_Leases = models.FloatField(null=True, blank=True, default=None)
    Deferred_Tax_Liability_Long_Term = models.FloatField(null=True, blank=True, default=None)
    Other_Long_Term_Debt = models.FloatField(null=True, blank=True, default=None)
    Common_Stock_at_par = models.FloatField(null=True, blank=True, default=None)
    Preferred_Stock_at_par = models.FloatField(null=True, blank=True, default=None)
    Paid_in_Capital_Common_Stock = models.FloatField(null=True, blank=True, default=None)
    Paid_in_Capital_Preferred_Stock = models.FloatField(null=True, blank=True, default=None)
    Other_net_rounding_adjustment_manual = models.FloatField(null=True, blank=True, default=None)
    Common_Dividend = models.FloatField(null=True, blank=True, default=None)
    Preferred_Dividend = models.FloatField(null=True, blank=True, default=None)
    Cash_from_Financing_Activities = models.FloatField(null=True, blank=True, default=None)
    Change_in_Cash = models.FloatField(null=True, blank=True, default=None)
    Beginning_Cash = models.FloatField(null=True, blank=True, default=None)
    Ending_Cash = models.FloatField(null=True, blank=True, default=None)
    

class Assumptions(models.Model):
         
    Worst = models.FloatField(null=True, blank=True, default=None)
    Base = models.FloatField(null=True, blank=True, default=None)
    Best = models.FloatField(null=True, blank=True, default=None)
    Name = models.TextField(null=True, blank=True, default=None)
      
       

