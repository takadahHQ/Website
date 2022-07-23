import datetime
from django import forms
from stories.models import Author, Chapter, Stories, Tag, Character, Editor, Author
from django.forms.widgets import NumberInput
from django.conf import settings

class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"
 
class DateTimeLocalField(forms.DateTimeField):
     
    # input_formats = [
    #     '%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
    #     '%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
    #     '%Y-%m-%d',             # '2006-10-25'
    #     '%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
    #     '%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
    #     '%m/%d/%Y',             # '10/25/2006'
    #     '%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
    #     '%m/%d/%y %H:%M',       # '10/25/06 14:30'
    #     '%m/%d/%y'
    # ]
    widget = DateTimeLocalInput(format="%Y-%m-%dT%H:%M", attrs={'class': 'textinput bg-white px-4 rounded-lg py-2 block border w-full text-gray-700 leading-normal focus:outline-none appearance-none border-gray-300'})

class StoryForm(forms.ModelForm):
    released_at = DateTimeLocalField(initial = datetime.date.today)

    class Meta:
        model = Stories
        fields = ('title','abbreviation', 'summary', 'cover', 'story_type', 'tags', 'language','genre','rating', 'released_at','status',)

# AuthorSet = inlineformset_factory(
#     Story,
#     settings.AUTH_USER_MODEL,
#     StoryForm,)

class ChapterForm(forms.ModelForm):
    # released_at = forms.DateTimeField(widgets = {'request_date': DateTimeInput(attrs={'type': 'datetime-local'}),})
    released_at = DateTimeLocalField(initial = datetime.date.today)

    class Meta:
        model = Chapter
        fields = ('title','position', 'text', 'authors_note', 'status', 'released_at', )


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('user',)

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('name', 'category')

class EditorForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = ('user',)