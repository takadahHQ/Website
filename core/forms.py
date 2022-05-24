from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users

from stories.models import Languages

class ColorInput(forms.TextInput):
    input_type = "color"
 
class ColorField(forms.Field):
    widget = ColorInput(attrs={'class': 'textinput bg-white px-4 rounded-lg py-2 block border w-full text-gray-700 leading-normal focus:outline-none appearance-none border-gray-300'})
    

class SignUpForm(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input px-4 m-2 py-3 rounded'})),
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class': 'form-input px-4 py-3 m-2 rounded'}))
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class': 'form-input px-4 py-3 m-2 rounded'}))
    #pseudonym = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'class': 'form-input px-4 py-3  m-2 rounded'}))

    class Meta:
        model = Users
        fields = ('username','pseudonym', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    # def __init__(self, *args, **kwargs):
    #   super(SignUpForm, self).__init__(*args, **kwargs)
    #   for field in self.fields:
    #      self.fields[field].widget.attrs['class'] = 'form-input input input-bordered input-accent w-full max-w-lg m-2 rounded'

class ProfileForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    pseudonym = forms.CharField(max_length=255, required=False, help_text='Optional.')
    bio = forms.CharField(required=False, help_text='Optional.')
    location = forms.CharField(max_length=30, required=False, help_text='Optional.')
    birth_date = forms.DateField(required=False, help_text='Optional.')
    profile_photo = forms.ImageField(max_length=2048, required=False, help_text='Optional.')
    # created_at = forms.DateTimeField(auto_now_add=True)
    # updated_at = forms.DateTimeField(auto_now=True)
    kyc_verified_at = forms.DateTimeField(required=False, help_text='Optional.', )
    language_id = forms.ModelChoiceField(queryset=Languages.objects.all(), empty_label="(Nothing)", help_text='Optional.')

    class Meta:
        model = Users
        fields =  '__all__'
        #fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )