from django import forms

from .models import Client, Credit, CreditType


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('client_id', 'Second_name', 'First_name', 'Third_name', 'Passport', 'Address', 'Salary')


class CreditTypeForm(forms.ModelForm):

    class Meta:
        model = CreditType
        fields = ('credit_type_id', 'credit_name', 'interest_rate', 'provision_condition')


class CreditForm(forms.ModelForm):

    class Meta:
        model = Credit
        fields = ('client_id', 'credit_type_id', 'submission_date', 'how_long', 'return_date', 'cost', 'is_payed')