from django.shortcuts import render, get_object_or_404, redirect
from scouts.models import Post, Image, File
from scouts.forms import PostForm, CommentForm, UploadFileForm
from accounts.models import User
from main_website.models import Article
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class PostList(LoginRequiredMixin, ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_posted')
    template_name = 'scouts/home.html' # <app>/<model>_<viewtype>.html
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context['articles'] = articles
        context['title'] = 'Home'
        return context

    def get_queryset(self):
        return Post.objects.all().order_by('-date_posted')

class UserPostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'scouts/user_posts.html'  # <app>/<model>_<viewtype>.html
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context['articles'] = articles
        context['title'] = 'Your Posts'
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

@login_required        
def post_detail(request, slug):
    template_name = "scouts/post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
    comments = post.scouts_blog_comments.filter(active=True).order_by('-date_posted')
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "articles": articles,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
            "title": 'Post Details',
        },
    )

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm     

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        #form.send_email()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context['articles'] = articles
        context['title'] = 'New Post'
        return context

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context['articles'] = articles
        context['title'] = 'Update Post'
        return context

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    success_url = '/'
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context['articles'] = articles
        context['title'] = 'Delete Post'
        return context

@login_required
def upload(request):
    articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'File Successfully Uploaded')
            return redirect('scoits_blog_file_upload')
    else:
        form = UploadFileForm()

    context = { 
        'title': 'Upload File',
        'articles': articles,
        'form': form
    }

    return render(request, 'scouts/file_upload.html', context)

class DownloadView(LoginRequiredMixin, generic.View):
    def get(self, request):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        file_collection = File.objects.all()
        context = { 
            'title': 'Downloads',
            'articles': articles,
            'file_collection': file_collection,
        }
        return render(request, 'scouts/file_download.html', context)

class AboutView(generic.View):
    def get(self, request):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context = { 
            'title': 'About',
            'articles': articles
        }
        return render(request, 'scouts/about.html', context)

class SearchView(generic.View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        queryset = Post.objects.all()
        query = request.GET.get('scouts_blog_search')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        context = {
            'queryset': queryset,
            'articles': articles
        }
        return render(request, 'scouts/search_results.html', context)