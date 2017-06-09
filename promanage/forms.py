from django import forms
from django.contrib.auth.models import User
from .models import Property

class PropertyForm(forms.ModelForm):

    thumbnail = forms.FileField(label='upload an image')
    class Meta:
        model = Property
        exclude=['user']
        widgets = {
            'proname': forms.TextInput(attrs={'class': 'form-control','placeholder':'eg:AnjanaResidency,Brundahanam..etc'}),
            'property_type': forms.Select(attrs={'class': 'form-control',}),
            'service_type': forms.Select(attrs={'class': 'form-control', }),
            'thumbnail': forms.FileInput(attrs={'class': 'btn btn-primary', }),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder':'eg:Guntur,vizag..etc'}),
            'location': forms.TextInput(attrs={'class': 'form-control','placeholder':'eg:MVP colony,A.T agraharam...etc'}),
            'address': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': '(optional)eg:1-146,opp:SBI..etc','rows':4,'columns':5}),
            'plan': forms.Select(attrs={'class': 'form-control'}),
        }