from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'qualification':forms.TextInput(attrs={'class':'form-control'}),
        'experience':forms.TextInput(attrs={'class':'form-control'}),
        'specialization':forms.TextInput(attrs={'class':'form-control'}),
        }
    

