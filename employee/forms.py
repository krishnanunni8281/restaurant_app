from django import forms
from employee.models import Staff,Food







class EmpStaffForm(forms.ModelForm):
    class Meta:
        model= Staff
        fields="__all__"

class EmpFoodForm(forms.ModelForm):
    class Meta:
        model=Food
        fields="__all__"