from django.shortcuts import render, get_object_or_404, redirect
from beavers.models import Post, File
from beavers.forms import PostForm, CommentForm, UploadFileForm
from accounts.models import User
from main_website.models import Article
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class PostList(LoginRequiredMixin, ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_posted')
    template_name = 'beavers/home.html' # <app>/<model>_<viewtype>.html
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
    template_name = 'beavers/user_posts.html'  # <app>/<model>_<viewtype>.html
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

class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    form_class = CommentForm
    template_name = "beavers/post_detail.html"

    def get_form(self):
        form = self.form_class(instance=self.object)
        return form

    def post(self, slug, *args, **kwargs): 
        new_comment = None
        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST) 
        if form.is_valid(): 
            # Create new_comment object but don't save to the database yet
            new_comment = form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            messages.warning(request, "Your comment is awaiting moderation, once moderated it will be published")
            return redirect('beavers_blog_post_detail', slug=slug) 
        else: 
            return render(request, self.template_name, {'form': form}) 

    def get_context_data(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, slug=slug)
        comments = post.beavers_blog_comments.filter(active=True).order_by('-date_posted')
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        
        post_likes = get_object_or_404(Post, slug=self.kwargs['slug'])
        total_likes = post_likes.total_likes()

        if post_likes.likes.filter(id=self.request.user.id).exists():
            liked = True
        else:
            liked = False

        context['liked'] = liked
        context['articles'] = articles
        context['comments'] = comments
        context['total_likes'] = total_likes
        context['title'] = 'Post Details'

        context.update({
            'comment_form': self.get_form(),
        })

        return context

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

def PostLikeView(request, slug):
    post = get_object_or_404(Post, slug=request.POST.get('beavers_blog_post_slug'))
    
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('beavers_blog_post_detail', args=[str(slug)]))

@login_required
def upload(request):
    articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'File Successfully Uploaded')
            return redirect('beavers_blog_file_upload')
    else:
        form = UploadFileForm()

    context = { 
        'title': 'Upload File',
        'articles': articles,
        'form': form
    }

    return render(request, 'beavers/file_upload.html', context)

class DownloadView(LoginRequiredMixin, generic.View):
    def get(self, request):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        file_collection = File.objects.all()
        context = { 
            'title': 'Downloads',
            'articles': articles,
            'file_collection': file_collection,
        }
        return render(request, 'beavers/file_download.html', context)

class AboutView(generic.View):
    def get(self, request):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context = { 
            'title': 'About',
            'articles': articles
        }
        return render(request, 'beavers/about.html', context)

class BadgePlacementView(generic.View):
    def get(self, request):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context = { 
            'title': 'Badge Placement',
            'articles': articles
        }
        return render(request, 'beavers/badge_placement.html', context)

class SearchView(generic.View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        queryset = Post.objects.all()
        query = request.GET.get('beavers_blog_search')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        context = {
            'queryset': queryset,
            'articles': articles
        }
        return render(request, 'beavers/search_results.html', context)