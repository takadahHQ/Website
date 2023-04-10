from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    ListView,
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.db.models import Count
from modules.stories.actions.user import (
    bookmark_story,
    get_all_ratings,
    get_chapter_by_id,
    get_language,
    get_packages,
    get_reviews_by_id,
    get_story_by_id,
    remove_review,
)
from modules.stories.forms import StoryForm, ChapterForm
from taggit.models import Tag
from modules.stories.models import (
    Chapter,
    Stories,
    Bookmark,
    Language,
    Genre,
    Rating,
    Type,
    Universe,
)
from modules.stories.views.mixins import HistoryMixin
from modules.stories.actions import (
    get_genre,
    get_stories_by_genre,
    get_tag,
    get_stories_by_tag,
    get_type,
    get_stories_by_type,
    like_story,
    dislike_story,
    follow_story,
    get_story,
    get_reviews,
    get_chapter,
    get_story_bookmarks,
)
from modules.stories.forms import (
    ReviewForm,
)
from django.contrib.auth.decorators import login_required


def storyLike(request, id):
    story = like_story(user=request.user, slug=id)
    return render(request, "stories/partials/like.html", {"story": story})


def storyDisLike(request, id):
    story = dislike_story(user=request.user, slug=id)
    return render(request, "stories/partials/dislike.html", {"story": story})


def storyBookmark(request, id):
    bookmarks, story = bookmark_story(user=request.user, slug=id)
    return render(
        request,
        "stories/partials/bookmark.html",
        {"bookmark": bookmarks, "story": story},
    )


def storyFollow(request, id):
    story = follow_story(user=request.user, slug=id)
    return render(request, "stories/partials/following.html", {"story": story})


# def showStory(request, id):
#     context = {}
#     template = ""
#     return render(request, template, context)


def showStory(request, type: str, slug: str):
    story = get_story(slug=slug, type=type)
    bookmark = get_story_bookmarks(story=story)
    review = ""
    recommendation = ""
    context = {"story": story, "bookmark": bookmark}
    template = "stories/readers/story_detail.html"
    return render(request, template, context)

    # class ShowStory(DetailView):
    #     template_name = "stories/readers/story_detail.html"
    #     context_object_name = "story"

    #     def get_queryset(self):
    #         return get_story(slug=self.kwargs.get("slug"),type=self.kwargs.get("type"))

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["review"] = get_reviews(story__slug=self.kwargs.get("slug"))
    #     return context


class ShowChapter(HistoryMixin, DetailView):
    model = Chapter
    template_name = "stories/readers/read.html"
    context_object_name = "story"

    def get_object(self):
        story = self.kwargs.get("story")
        type = self.kwargs.get("type")
        chapter = self.kwargs.get("slug")
        user = self.request.user.id
        return get_chapter(story=story, chapter=chapter, user=user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["reviewed"], context["reviews_count"] = get_reviews(
            story=self.kwargs.get("story"), chapter=self.kwargs.get("slug")
        )
        context["packages"] = get_packages(
            story=self.kwargs.get("story"), chapter=self.kwargs.get("slug")
        )
        return context


class ShowTag(ListView):
    model = Stories
    template_name = "stories/tags.html"
    context_object_name = "story"

    def get_queryset(self):
        return get_stories_by_tag(self.kwargs.get("slug"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["tag"] = get_tag(slug=self.kwargs.get("slug"))
        return context


class ShowGenre(ListView):
    model = Stories
    template_name = "stories/genres.html"
    context_object_name = "story"

    def get_queryset(self):
        # Stories.objects.filter(stories__genre=self.kwargs.get('pk')).exclude(stories__status='pending')#.order_by('-created_at')[:15]
        return get_stories_by_genre(slug=self.kwargs.get("slug"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["genre"] = get_genre(self.kwargs.get("slug"))
        return context


class ShowRating(ListView):
    model = Rating
    template_name = "stories/ratings.html"
    context_object_name = "story"

    def get_queryset(self):
        return get_all_ratings(slug=self.kwargs.get("slug"))


class ShowType(ListView):
    model = Stories
    template_name = "stories/type.html"
    context_object_name = "story"

    def get_queryset(self):
        return get_stories_by_type(self.kwargs.get("slug"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["type"] = get_type(self.kwargs.get("slug"))
        return context


class ShowLanguage(ListView):
    model = Language
    template_name = "stories/language.html"
    context_object_name = "story"

    def get_queryset(self):
        return get_language(self.kwargs.get("slug"))


def update_review(request, review):
    review = get_reviews_by_id(review=review)
    form = ReviewForm(request.POST or None, instance=review)
    if request.method == "POST":
        if form.is_valid():
            review = form.save()
            return redirect("stories:detail-review", review=review.id)
    context = {
        "reviewform": form,
        "review": review,
    }
    return render(request, "stories/reviews/form.html", context)


def detail_review(request, review):
    review = get_reviews_by_id(review)
    # reviewed, reviews_count = get_reviews(story=story, chapter=chapter)
    context = {
        "review": review,
    }
    return render(request, "stories/reviews/view.html", context)


def delete_review(request, review):
    remove_review(review)
    return HttpResponse("")


@login_required
def save_review(request, story, chapter):
    user = request.user
    story = get_story_by_id(story)
    chapter = get_chapter_by_id(user=request.user, chapter=chapter)
    reviewed, reviews_count = get_reviews(story=story, chapter=chapter)

    form = ReviewForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            review = form.save(commit=False)
            review.story = story
            review.chapter = chapter
            # if review_id:
            #     review.parent = review_id
            review.user = request.user
            review.save()
            return redirect("stories:detail-review", review=review.id)
        else:
            return render(request, "stories/reviews/form.html", context={"aform": form})
    else:
        return render(
            request,
            "stories/reviews/form.html",
            context={
                "reviewform": form,
                "reviews": reviewed,
                "reviews_count": reviews_count,
                "story": story,
            },
        )


def refresh_reviews(request, story, chapter):
    story = get_story_by_id(story)
    chapter = get_chapter_by_id(user=request.user, chapter=chapter)
    reviewed, reviews_count = get_reviews(story=story, chapter=chapter)
    context = {
        "reviewed": reviewed,
        "reviews_count": reviews_count,
        "story": chapter,
    }
    return render(request, "stories/includes/comment.html", context)


@login_required
def reply_review(request, review):
    review = get_reviews_by_id(review)
    user = request.user
    story = get_story_by_id(review.story)
    chapter = get_chapter_by_id(user=request.user, chapter=review.chapter)
    form = ReviewForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            review = form.save(commit=False)
            review.story = story
            review.chapter = chapter
            review.parent = review.id
            review.user = request.user
            review.save()
            return redirect("stories:detail-review", review=review.id)
        else:
            return render(request, "stories/reviews/form.html", context={"aform": form})
    else:
        return redirect(
            "stories:read", type=story.story_type, story=story, slug=chapter.slug
        )


class userDashboard(LoginRequiredMixin, TemplateView):
    template_name = "stories/user.html"
    model = Stories

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["total_likes"] = self.total_likes()
        context["published"] = self.story_list()
        context["stats"] = self.story_stats()
        context["earnings"] = self.story_earnings()
        return context

    def total_likes(self):
        # liked = Stories.objects.filter(authors=self.request.user).annotate(total_likes=Sum(likes))
        likes = Stories.objects.filter(author=self.request.user).aggregate(
            total_likes=Count("likes")
        )["total_likes"]
        # all_stories = self.request.user.authors.all()
        # stotal_likes_received = all_stories.aggregate(total_likes=Count('likes'))['total_likes']
        return likes

    # def story_list(self):
    #     #    story =  Stories.objects.exclude(status='pending').exclude(status='draft').filter(author__user__in=self.request.user)
    #     story = get_stories_by_author(user=self.request.user)
    #     return story

    def story_stats(self):
        likes = get_author_stories_likes(author=self.request.user)
        dislikes = get_author_stories_dislikes(author=self.request.user)
        reviews = get_author_stories_reviews(author=self.request.user)
        views = get_author_stories_views(author=self.request.user)
        stats = {
            "views": {"result": views, "updated": "2 hours ago"},
            "likes": {"result": likes, "updated": "2 minutes ago"},
            "dislikes": {"result": dislikes, "updated": "21 days ago"},
            "reviews": {"result": reviews, "updated": "2 seconds ago"},
        }
        return stats

    # def story_earnings(self):
    #     daily = get_daily_earnings(author=self.request.user)
    #     weekly = get_weekly_earnings(author=self.request.user)
    #     monthly = get_monthly_earnings(author=self.request.user)
    #     stats = {
    #         "daily": {"amount": daily},
    #         "weekly": {"amount": weekly},
    #         "monthly": {"amount": monthly},
    #     }
    #     return stats
