# views.py

from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from modules.roadmap.models import Feature, Vote, Comment
from django.views.generic import DetailView
from django.http import HttpResponse


def roadmap(request):
    features = Feature.objects.all()
    return render(request, "roadmap.html", {"features": features})


# @require_POST
def vote(request, pk, action):
    feature = Feature.objects.get(id=pk)
    user = request.user
    if action == "upvote":
        Vote.objects.update_or_create(
            user=user, feature=feature, defaults={"vote": True}
        )
    elif action == "downvote":
        Vote.objects.update_or_create(
            user=user, feature=feature, defaults={"vote": False}
        )
    feature = Feature.objects.get(id=pk)
    score = feature.get_votes()
    # return JsonResponse({"score": score})
    print(feature)
    html_text = (
        f"<span class='score mx-auto' data-feature='{ feature.id }'>{ score }</span>"
    )
    return HttpResponse(html_text)


@require_POST
def comment(request):
    feature_id = request.POST["feature"]
    content = request.POST["content"]
    feature = Feature.objects.get(id=feature_id)
    user = request.user
    Comment.objects.create(user=user, feature=feature, content=content)
    return JsonResponse({"success": True})


# views.py


def comments(request, pk):
    feature = Feature.objects.get(id=pk)
    comments = feature.comments.all()
    return render(request, "comments.html", {"comments": comments})


def replies(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    replies = comment.replies.all()
    return render(request, "replies.html", {"replies": replies})


class FeatureDetailView(DetailView):
    model = Feature
    template_name = "feature_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feature = self.object
        context["comments"] = feature.comments.filter(parent__isnull=True)
        return context
