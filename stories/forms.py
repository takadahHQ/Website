from dataclasses import fields
from platform import release
from django import forms
from stories.models import Author, Chapter, Stories, Tag, Character, Editor, Author
from django.forms.widgets import NumberInput
from django.conf import settings


# class Inline(InlineFormSetFactory):
#     model = Contact
#    fields = ['name', 'email']


class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"
 
class DateTimeLocalField(forms.DateTimeField):
     
    input_formats = [
        "%Y-%m-%dT%H:%M:%S", 
        "%Y-%m-%dT%H:%M:%S.%f", 
        "%Y-%m-%dT%H:%M"
    ]
    widget = DateTimeLocalInput(format="%Y-%m-%dT%H:%M", attrs={'class': 'textinput bg-white px-4 rounded-lg py-2 block border w-full text-gray-700 leading-normal focus:outline-none appearance-none border-gray-300'})

class StoryForm(forms.ModelForm):
    released_at = DateTimeLocalField()

    # def clean_authors(self):
    #     email = self.cleaned_data.get('authors')
    #     current_user_email = User.email
    #     if User.objects.filter(email__iexact=author).exclude(email__iexact=current_user_email).count() > 0:
    #         raise forms.ValidationError('This email address is already in use.'
    #                                     'Please supply a different email address.')
    # return email

    class Meta:
        model = Stories
        fields = ('title','abbreviation', 'summary', 'authors', 'cover', 'story_type', 'tags', 'language','genre','rating', 'released_at','status',)

# AuthorSet = inlineformset_factory(
#     Story,
#     settings.AUTH_USER_MODEL,
#     StoryForm,)

class ChapterForm(forms.ModelForm):
    #released_at = forms.DateTimeField(widget=NumberInput(attrs={'type': 'datetime-local'}), input_formats=['%d/%m/%Y %H:%M'])
    released_at = DateTimeLocalField()

    class Meta:
        model = Chapter
        fields = ('title','position', 'text', 'authors_note', 'status', 'released_at', )


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('story', 'user')

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('name', 'category')

class EditorForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = ('story', 'user')