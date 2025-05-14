from django import forms
from .models import Guardian

class GuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = '__all__'

        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'relationship': forms.Select(choices=[
                ('Mother', 'Mother'),
                ('Father', 'Father'),
                ('Guardian', 'Guardian')
            ], attrs={'class': 'form-control'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
