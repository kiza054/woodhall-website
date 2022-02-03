import calendar
from taggit.models import Tag
from django.db.models import Q
from django.conf import settings
from django.views import generic
from django.contrib import messages
from main_website.utils import Calendar, get_date, prev_month, next_month
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta, date
from django.contrib.auth.decorators import login_required
from main_website.models import Article, Event, ImageGallery, ImageGalleryCategory
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from main_website.forms import ArticleForm, WaitingListForm, EventForm, UploadImageForm, AddImageCategoryForm

class IndexView(generic.View):
    def get(self, request):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context = {
            'title': 'Home',
            'articles': articles
        }
        return render(request, 'main_website/home.html', context)

class AboutView(generic.View):
    def get(self, request):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context = { 
            'title': 'About',
            'articles': articles,
            'api_key': settings.GOOGLE_MAPS_API_KEY
        }
        return render(request, 'main_website/about.html', context)

class ArticleList(ListView):
    model = Article
    template_name = 'main_website/latest_news.html'
    
    def get_context_data(self, **kwargs):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context = super().get_context_data(**kwargs)
        context['articles'] = articles
        context['title'] = 'Latest News'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'main_website/new_article.html'  # <app>/<model>_<viewtype>.html   

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context = super().get_context_data(**kwargs)
        context['articles'] = articles
        context['title'] = 'New Article'
        return context

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'main_website/new_article.html'  # <app>/<model>_<viewtype>.html 

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context['articles'] = articles
        context['title'] = 'Update Article'
        return context

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    success_url = '/'
    model = Article

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context['articles'] = articles
        context['title'] = 'Delete Article'
        return context

@login_required        
def article_detail(request, slug):
    template_name = "main_website/news_article_detail.html"
    article = get_object_or_404(Article, slug=slug)
    articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]

    return render(
        request,
        template_name,
        {
            "article": article,
            "articles": articles,
            "title": 'Article Details',
        },
    )

def waiting_list_register(request):
    articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
    if request.method == 'POST':
        form = WaitingListForm(request.POST)
        if form.is_valid():
            form.section_of_interest = request.POST.get('section_of_interest')
            form.save()
            messages.success(request, f'Your child has been added to the waiting list, we\'ll get back to you as soon as possible!')
            return redirect('main_website_home')
    else:
        form = WaitingListForm()
    
    context = {
        'title': 'Waiting List',
        'articles': articles,
        'form': form,
    }

    return render(request, 'main_website/waiting_list_form.html', context)

class HelpUsView(generic.View):
    def get(self, request):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context = {
            'title': 'Help Us',
            'articles': articles
        }
        return render(request, 'main_website/help_us.html', context)

class DonateView(generic.View):
    def get(self, request):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context = {
            'title': 'Ways to Donate',
            'articles': articles
        }
        return render(request, 'main_website/donate.html', context)

class ContactUsView(generic.View):
    def get(self, request):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context = {
            'title': 'Contact Us',
            'articles': articles
        }
        return render(request, 'main_website/contact_us.html', context)

class SearchView(generic.View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        queryset = Article.objects.all()
        query = request.GET.get('search')

        if query:
            queryset = queryset.filter(
                Q(article_name__icontains=query) |
                Q(content__icontains=query)
            ).distinct()

        context = {
            'queryset': queryset,
            'articles': articles
        }

        return render(request, 'main_website/search_results.html', context)

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['title'] = 'Calendar'
        return context

class EventView(LoginRequiredMixin, generic.View):
    def get(self, request, event_id=None):
        instance = Event()
        if event_id:
            instance = get_object_or_404(Event, pk=event_id)
        else:
            instance = Event()

        form = EventForm()

        context = { 
            'form': form,
            'instance': instance,
            'title': 'New Event',
        }
        return render(request, 'calendar/event.html', context)

class EditEventView(LoginRequiredMixin, generic.View):
    def get(self, request, event_id=None):
        instance = Event()
        if event_id:
            instance = get_object_or_404(Event, pk=event_id)
        else:
            instance = Event()

        form = EventForm()

        context = { 
            'form': form,
            'instance': instance,
            'title': 'Edit Event',
        }
        return render(request, 'calendar/edit_event.html', context)

    def post(self, request):
        instance = Event()
        form = EventForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('main_website_calendar')

class TaggedView(LoginRequiredMixin, generic.View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        common_tags = Article.tags.most_common()[:4]
        # Filter articles by tag name  
        articles = Article.objects.filter(tags=tag)
        context = {
            'tag': tag,
            'articles': articles,
            'common_tags': common_tags
        }
        return render(request, 'main_website/news_article_tags.html', context)

class ImageGalleryView(LoginRequiredMixin, generic.View):
    def get(self, request):
        category = request.GET.get('category')
        if category == None:
            images = ImageGallery.objects.all()
        else:
            images = ImageGallery.objects.filter(category__name=category)

        categories = ImageGalleryCategory.objects.all()
        context = {
            'images': images,
            'categories': categories,
            'title': 'Image Gallery'
        }
        return render(request, 'main_website/image_gallery.html', context)

class ImageDetailView(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        images = ImageGallery.objects.get(id=pk)
        context = {
            'images': images,
            'title': 'Image Details'
        }
        return render(request, 'main_website/image_detail.html', context)

class ImageAddView(LoginRequiredMixin, generic.View):
    def get(self, request):
        form = UploadImageForm()
        context = {
            'form': form,
            'title': 'Add Image'
        }
        return render(request, 'main_website/image_upload.html', context)

    def post(self, request):
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image Successfully Uploaded')
            return redirect('main_website_gallery')

class ImageCategoryAddView(LoginRequiredMixin, generic.View):
    def get(self, request):
        form = AddImageCategoryForm()
        context = {
            'form': form,
            'title': 'Add Category'
        }
        return render(request, 'main_website/image_add_category.html', context)

    def post(self, request):
        form = AddImageCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Successfully Added')
            return redirect('main_website_gallery')

def error_403_view(request, exception):
    data = {}
    articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
    context = {
        'title': '404 Error',
        'articles': articles,
    }
    return render(request, 'main_website/errors/403_error.html', context, status=403)

def error_404_view(request, exception):
    data = {}
    articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
    context = {
        'title': '404 Error',
        'articles': articles,
    }
    return render(request, 'main_website/errors/404_error.html', context, status=404)

def error_500_view(request, *args, **argv):
    data = {}
    articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
    context = {
        'title': '500 Error',
        'articles': articles,
    }
    return render(request, 'main_website/errors/500_error.html', context, status=500)