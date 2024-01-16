from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ( 
        ListView, 
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
)
from .models import Post

# from django.http import HttpResponse
# Create your views here.
# def index(response):
#     return HttpResponse("<h1> tech with tim! <h1>")

# def v1(response):
#     return HttpResponse("<h1> view1 <h1>")

# posts = [
#     {
#         'author':'CoreyMS',
#         'title' : 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author':'Jane Doe',
#         'title' : 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 29, 2018'
#     }

# ]
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,"main/home.html",context)

class PostListView(ListView):
    model = Post    # this will tell,to query the post model.
    template_name =  'main/home.html'  # <app>/<model>_<viewtype>.html 
                                      # listview class knows to check for this template instead of checking for default naming pattern template.
    context_object_name = 'posts'  # with this listview class know that the variable is posts to loopover in the template.
    ordering = ['-date_posted']
    paginate_by = 3

class UserPostListView(ListView):
    model = Post
    template_name = 'main/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'main/about.html',{'title':"baby"})