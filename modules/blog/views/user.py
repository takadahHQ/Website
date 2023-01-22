from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from modules.blog.models import Post, Category
from django.views import generic
from django.http import Http404


def page(request, category=None, slug=None):

    # category = get_object_or_404(Category, slug=path)
    # queryset = Post.objects.filter(category__slug=category)
    # blog = get_object_or_404(Post, slug=slug)
    try:
        blog = Post.objects.filter(category__slug=category).get(slug=slug)
    except:
        raise Http404("No Post matches the given query.")

    return render(request, "blog/blog-post.html", {"blog": blog})


def list(request):
    blogs = Post.objects.order_by("-published_at")[:5]
    context = {"blogs": blogs}
    return render(request, "blog/blog-list.html", context)


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/blog-list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Post.objects.order_by("-published_at")[:5]


class CategoryListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/category-list.html"
    context_object_name = "categories"

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs["category"])
        return Post.objects.filter(category=self.category).order_by("-published_at")[:5]


class PostView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/blog-post.html"

    # def get_queryset(self):
    #      return Post.objects.filter(category__slug=category).get(slug=slug)


def view_a(request):
    return render(request, "view_a.html")
