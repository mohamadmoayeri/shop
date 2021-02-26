from django import forms

from .models import User

class eidit_profile_form(forms.ModelForm):

    class Meta:
        model=User

        fields=['avatar','username','email','first_name','last_name','phone']

        widgets={
            'avatar':forms.FileInput
        }

        labels={
            'avatar':'Profile photo'
        }

