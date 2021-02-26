from django import forms

class register(forms.Form):

    username=forms.SlugField(allow_unicode=False,max_length=25,label='username')

    email=forms.EmailField(label='email',widget=forms.EmailInput)

    password=forms.SlugField(allow_unicode=False,widget=forms.PasswordInput)

    password2=forms.SlugField(label='Re-type Password',allow_unicode=False, widget=forms.PasswordInput)

 



class PasswordResetForm(forms.Form):

    email=forms.EmailField(widget=forms.EmailInput)