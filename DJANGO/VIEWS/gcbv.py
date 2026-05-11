#There are some generic CBV defined by django to help us build fast
from django.views.generic

#read data

from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 5
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = Post.objects.all()

        # optional filtering (example: query param থেকে search)
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "All Blog Posts"
        context['total_posts'] = Post.objects.count()
        return context