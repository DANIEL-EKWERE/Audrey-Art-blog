from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import *
from django import forms
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm, self).__init__(*args,**kwargs)
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label
        self.fields['first_name'].widget.attrs['placeholder'] =self.fields['first_name'].label
        self.fields['last_name'].widget.attrs['placeholder'] =self.fields['last_name'].label
        self.fields['password1'].widget.attrs['placeholder'] =self.fields['password1'].label
        self.fields['password2'].widget.attrs['placeholder'] =self.fields['password2'].label

    class Meta:
        model = myuser
        fields = ('email','first_name','last_name','password1','password2')

class MyLoginForm(AuthenticationForm):
    username = forms.EmailField(label= 'Email',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(max_length=33, widget=forms.PasswordInput(attrs={'placeholder':'password'}))

    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': _(
            "Please enter the correct Email and password for a Customers"
            "account. Note that both fields are case-sensitive "

        ),
    }

# class CustomerLoginForm(AuthenticationForm):
#     username = forms.CharField(label='Email', widget=forms.TextInput(attrs={'placeholder':'Email'}))
#     password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

#     error_messages = {
#         **AuthenticationForm.error_messages,
#         'invalid_login': _(
#             "Please enter the correct Email and password for a Customers"
#             "account. Note that both fields are case-sensitive "

#         ),
#     }


'''
class MyLoginForm(AuthenticationForm):
    user = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    '''

''' comment form'''

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields= ('body','parent')


class CreateBook(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = [
            'image',
            'title',
            'author',
            'body',
            'category',
            'slug',
            'tags',
            'status',
        ]
