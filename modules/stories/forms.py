import datetime
from django import forms
from modules.stories.models import (
    Author,
    Chapter,
    Stories,
    Character,
    Editor,
    Author,
    Review,
)
from django.forms.widgets import NumberInput, TextInput, Select, CheckboxInput
from django.conf import settings


class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"


class DateTimeLocalField(forms.DateTimeField):

    widget = DateTimeLocalInput(
        format="%Y-%m-%dT%H:%M",
        attrs={
            "class": "textinput bg-white px-4 rounded-lg py-2 block border w-full text-gray-700 leading-normal focus:outline-none appearance-none border-gray-300"
        },
    )


class StoryForm(forms.ModelForm):
    released_at = DateTimeLocalField(initial=datetime.date.today)

    class Meta:
        model = Stories
        fields = (
            "title",
            "abbreviation",
            "summary",
            "cover",
            "story_type",
            "tags",
            "language",
            "genre",
            "rating",
            "released_at",
            "status",
        )
        # widgets= {
        #     "language": Select(attrs={'class': 'bg-white focus:outline-none border border-gray-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-gray-700'}),
        #     "story_type": Select(attrs={'class': 'bg-white focus:outline-none border border-gray-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-gray-700'}),
        #     "genre": Select(attrs={'class': 'bg-white focus:outline-none border border-gray-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-gray-700'}),
        #     "rating": Select(attrs={'class': 'bg-white focus:outline-none border border-gray-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-gray-700'}),
        #     "status": Select(attrs={'class': 'bg-white focus:outline-none border border-gray-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-gray-700'}),
        #     "tags": TextInput(attrs={'class': 'textinput bg-white px-4 rounded-lg py-2 block border w-full text-gray-700 leading-normal focus:outline-none appearance-none border-gray-300'})
        # }


# AuthorSet = inlineformset_factory(
#     Story,
#     settings.AUTH_USER_MODEL,
#     StoryForm,)


class ChapterForm(forms.ModelForm):
    # released_at = forms.DateTimeField(widgets = {'request_date': DateTimeInput(attrs={'type': 'datetime-local'}),})
    released_at = DateTimeLocalField(initial=datetime.date.today)

    class Meta:
        model = Chapter
        fields = (
            "title",
            "position",
            "text",
            "authors_note",
            "status",
            "released_at",
        )


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["user"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["text", "parent", "user"]
        exclude = ("user", "story", "chapter")


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ("name", "category")


class EditorForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = ["user"]
