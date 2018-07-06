# Generated by Django 2.0.6 on 2018-07-06 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assumptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Worst', models.FloatField(blank=True, default=None, null=True)),
                ('Base', models.FloatField(blank=True, default=None, null=True)),
                ('Best', models.FloatField(blank=True, default=None, null=True)),
                ('Name', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Historical_Balance_Sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Historical_Dates', models.CharField(max_length=30)),
                ('Cash', models.FloatField(blank=True, default=None, null=True)),
                ('Marketable_Securities', models.FloatField(blank=True, default=None, null=True)),
                ('Accounts_Receivables', models.FloatField(blank=True, default=None, null=True)),
                ('Allowance_for_Doubtful_Accounts', models.FloatField(blank=True, default=None, null=True)),
                ('Net_Accounts_Receivables', models.FloatField(blank=True, default=None, null=True)),
                ('Inventories', models.FloatField(blank=True, default=None, null=True)),
                ('Inventory_Reserves', models.FloatField(blank=True, default=None, null=True)),
                ('Net_Inventories', models.FloatField(blank=True, default=None, null=True)),
                ('Prepaid_Assets', models.FloatField(blank=True, default=None, null=True)),
                ('Other_Current_Assets', models.FloatField(blank=True, default=None, null=True)),
                ('Total_Current_Assets', models.FloatField(blank=True, default=None, null=True)),
                ('Property_Plant_Equipment', models.FloatField(blank=True, default=None, null=True)),
                ('Accumulated_Depreciation', models.FloatField(blank=True, default=None, null=True)),
                ('Net_PPE', models.FloatField(blank=True, default=None, null=True)),
                ('Goodwill', models.FloatField(blank=True, default=None, null=True)),
                ('Impairment', models.FloatField(blank=True, default=None, null=True)),
                ('Net_Goodwill', models.FloatField(blank=True, default=None, null=True)),
                ('Intellectual_Property', models.FloatField(blank=True, default=None, null=True)),
                ('Accumulated_Amortization', models.FloatField(blank=True, default=None, null=True)),
                ('Net_IP', models.FloatField(blank=True, default=None, null=True)),
                ('Net_Long_Term_Assets', models.FloatField(blank=True, default=None, null=True)),
                ('Total_Assets', models.FloatField(blank=True, default=None, null=True)),
                ('Accounts_Payables', models.FloatField(blank=True, default=None, null=True)),
                ('Accrued_Liabilities', models.FloatField(blank=True, default=None, null=True)),
                ('Revolver', models.FloatField(blank=True, default=None, null=True)),
                ('Income_Taxes_Payable', models.FloatField(blank=True, default=None, null=True)),
                ('Current_Portion_of_Deferred_Tax_Liabilities', models.FloatField(blank=True, default=None, null=True)),
                ('Other_Current_Liabilities', models.FloatField(blank=True, default=None, null=True)),
                ('Current_Portion_of_Long_Term_Funded_Debt', models.FloatField(blank=True, default=None, null=True)),
                ('Current_Portion_of_Capitalized_Leases', models.FloatField(blank=True, default=None, null=True)),
                ('Other_Rounding_Difference', models.FloatField(blank=True, default=None, null=True)),
                ('Common_Dividend_Payable', models.FloatField(blank=True, default=None, null=True)),
                ('Preferred_Dividend_Payable', models.FloatField(blank=True, default=None, null=True)),
                ('Total_Current_Liabilities', models.FloatField(blank=True, default=None, null=True)),
                ('Long_Term_Funded_Debt', models.FloatField(blank=True, default=None, null=True)),
                ('Long_Term_Capital_Leases', models.FloatField(blank=True, default=None, null=True)),
                ('Deferred_Tax_Liability_Long_Term', models.FloatField(blank=True, default=None, null=True)),
                ('Other_Long_Term_Debt', models.FloatField(blank=True, default=None, null=True)),
                ('Total_Long_Term_Debt', models.FloatField(blank=True, default=None, null=True)),
                ('Total_Liabilities', models.FloatField(blank=True, default=None, null=True)),
                ('Common_Stock_at_par', models.FloatField(blank=True, default=None, null=True)),
                ('Preferred_Stock_at_par', models.FloatField(blank=True, default=None, null=True)),
                ('Paid_in_Capital_Common_Stock', models.FloatField(blank=True, default=None, null=True)),
                ('Paid_in_Capital_Preferred_Stock', models.FloatField(blank=True, default=None, null=True)),
                ('Current_Period_Net_Income', models.FloatField(blank=True, default=None, null=True)),
                ('Retained_Earnings', models.FloatField(blank=True, default=None, null=True)),
                ('Common_Dividend', models.FloatField(blank=True, default=None, null=True)),
                ('Preferred_Dividend', models.FloatField(blank=True, default=None, null=True)),
                ('Total_Equity', models.FloatField(blank=True, default=None, null=True)),
                ('Total_Liabilities_and_Equity', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Historical_Cash_Flow_Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Historical_Dates', models.CharField(max_length=30)),
                ('Net_Income', models.FloatField(blank=True, default=None, null=True)),
                ('Depreciation', models.FloatField(blank=True, default=None, null=True)),
                ('Goodwill_Impairment', models.FloatField(blank=True, default=None, null=True)),
                ('Amortization', models.FloatField(blank=True, default=None, null=True)),
                ('Change_in_Allowance_for_Doubtful_Accounts', models.FloatField(blank=True, default=None, null=True)),
                ('Change_in_Inventory_Reserve', models.FloatField(blank=True, default=None, null=True)),
                ('Cash_from_Operations', models.FloatField(blank=True, default=None, null=True)),
                ('Marketable_Securities', models.FloatField(blank=True, default=None, null=True)),
                ('Accounts_Receivables', models.FloatField(blank=True, default=None, null=True)),
                ('Inventories', models.FloatField(blank=True, default=None, null=True)),
                ('Prepaid_Assets', models.FloatField(blank=True, default=None, null=True)),
                ('Other_Current_Assets', models.FloatField(blank=True, default=None, null=True)),
                ('Accounts_Payables', models.FloatField(blank=True, default=None, null=True)),
                ('Accrued_Liabilities', models.FloatField(blank=True, default=None, null=True)),
                ('Revolver', models.FloatField(blank=True, default=None, null=True)),
                ('Income_Taxes_Payable', models.FloatField(blank=True, default=None, null=True)),
                ('Current_Portion_of_Deferred_Tax_Liabilities', models.FloatField(blank=True, default=None, null=True)),
                ('Other_Current_Liabilities', models.FloatField(blank=True, default=None, null=True)),
                ('Current_Portion_of_Long_Term_Funded_Debt', models.FloatField(blank=True, default=None, null=True)),
                ('Current_Portion_of_Capitalized_Leases', models.FloatField(blank=True, default=None, null=True)),
                ('Other_Rounding_Difference', models.FloatField(blank=True, default=None, null=True)),
                ('Common_Dividend_Payable', models.FloatField(blank=True, default=None, null=True)),
                ('Preferred_Dividend_Payable', models.FloatField(blank=True, default=None, null=True)),
                ('Cash_from_Working_Capital', models.FloatField(blank=True, default=None, null=True)),
                ('Capital_Expenditures', models.FloatField(blank=True, default=None, null=True)),
                ('Goodwill', models.FloatField(blank=True, default=None, null=True)),
                ('Intangible_Assets', models.FloatField(blank=True, default=None, null=True)),
                ('Cash_from_Investing_Activities', models.FloatField(blank=True, default=None, null=True)),
                ('Long_Term_Funded_Debt', models.FloatField(blank=True, default=None, null=True)),
                ('Long_Term_Capital_Leases', models.FloatField(blank=True, default=None, null=True)),
                ('Deferred_Tax_Liability_Long_Term', models.FloatField(blank=True, default=None, null=True)),
                ('Other_Long_Term_Debt', models.FloatField(blank=True, default=None, null=True)),
                ('Common_Stock_at_par', models.FloatField(blank=True, default=None, null=True)),
                ('Preferred_Stock_at_par', models.FloatField(blank=True, default=None, null=True)),
                ('Paid_in_Capital_Common_Stock', models.FloatField(blank=True, default=None, null=True)),
                ('Paid_in_Capital_Preferred_Stock', models.FloatField(blank=True, default=None, null=True)),
                ('Other_net_rounding_adjustment_manual', models.FloatField(blank=True, default=None, null=True)),
                ('Common_Dividend', models.FloatField(blank=True, default=None, null=True)),
                ('Preferred_Dividend', models.FloatField(blank=True, default=None, null=True)),
                ('Cash_from_Financing_Activities', models.FloatField(blank=True, default=None, null=True)),
                ('Change_in_Cash', models.FloatField(blank=True, default=None, null=True)),
                ('Beginning_Cash', models.FloatField(blank=True, default=None, null=True)),
                ('Ending_Cash', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Historical_Income_Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Historical_Dates', models.CharField(max_length=30)),
                ('Revenue', models.FloatField(blank=True, default=None, null=True)),
                ('COGS', models.FloatField(blank=True, default=None, null=True)),
                ('Gross_Margin', models.FloatField(blank=True, default=None, null=True)),
                ('Selling_Marketing', models.FloatField(blank=True, default=None, null=True)),
                ('Research_Development', models.FloatField(blank=True, default=None, null=True)),
                ('General_Administrative', models.FloatField(blank=True, default=None, null=True)),
                ('Total_Operating_Expense', models.FloatField(blank=True, default=None, null=True)),
                ('EBITDA', models.FloatField(blank=True, default=None, null=True)),
                ('Depreciation', models.FloatField(blank=True, default=None, null=True)),
                ('Goodwill_Impairment', models.FloatField(blank=True, default=None, null=True)),
                ('Amortization', models.FloatField(blank=True, default=None, null=True)),
                ('Allowance_for_Doubtful_Accounts', models.FloatField(blank=True, default=None, null=True)),
                ('Inventory_Reserve', models.FloatField(blank=True, default=None, null=True)),
                ('EBIT', models.FloatField(blank=True, default=None, null=True)),
                ('Interest_Expense', models.FloatField(blank=True, default=None, null=True)),
                ('Interest_Income', models.FloatField(blank=True, default=None, null=True)),
                ('Income_before_Income_Taxes', models.FloatField(blank=True, default=None, null=True)),
                ('Current_Income_Tax', models.FloatField(blank=True, default=None, null=True)),
                ('Deferred_Income_Tax', models.FloatField(blank=True, default=None, null=True)),
                ('Total_Income_Tax_Provision', models.FloatField(blank=True, default=None, null=True)),
                ('Net_Income', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
    ]
