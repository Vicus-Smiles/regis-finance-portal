from django import forms
from .models import AcademicHistory

class AcademicHistoryForm(forms.ModelForm):
    class Meta:
        model = AcademicHistory
        fields = '__all__'

        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'previous_school': forms.TextInput(attrs={'class': 'form-control'}),
            'grade_obtained': forms.TextInput(attrs={'class': 'form-control'}),
            'pre_entry_test': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'orientation_done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'registration_complete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
