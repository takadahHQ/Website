from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Stories


class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        story = get_object_or_404(Stories, pk=self.kwargs["pk"])
        return self.request.user.is_authenticated and (
            story.author.filter(id=self.request.user.id).exists()
            or story.editor.filter(id=self.request.user.id).exists()
            or story.translator.filter(id=self.request.user.id).exists()
        )

    def handle_no_permission(self):
        raise Http404("Can't Access Any Such Story")
