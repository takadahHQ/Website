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
from taggit.forms import TagWidget


class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"


class DateTimeLocalField(forms.DateTimeField):
    widget = DateTimeLocalInput(
        format="%Y-%m-%dT%H:%M",
        attrs={
            "class": "textinput bg-mono-50 px-4 rounded-lg py-2 block border w-full text-mono-700 leading-normal focus:outline-none appearance-none border-mono-300"
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
        widgets = {
            #     "language": Select(attrs={'class': 'bg-mono-50 focus:outline-none border border-mono-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-mono-700'}),
            #     "story_type": Select(attrs={'class': 'bg-mono-50 focus:outline-none border border-mono-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-mono-700'}),
            #     "genre": Select(attrs={'class': 'bg-mono-50 focus:outline-none border border-mono-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-mono-700'}),
            #     "rating": Select(attrs={'class': 'bg-mono-50 focus:outline-none border border-mono-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-mono-700'}),
            #     "status": Select(attrs={'class': 'bg-mono-50 focus:outline-none border border-mono-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal text-mono-700'}),
            "tags": TagWidget(
                attrs={
                    "class": "tagify textinput bg-mono-50 px-4 rounded-lg py-2 block border w-full text-mono-700 leading-normal focus:outline-none appearance-none border-mono-300"
                }
            )
        }


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
