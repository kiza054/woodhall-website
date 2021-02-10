from django.views import generic
from accounts.models import User
from django.contrib import messages
from main_website.models import Article
from accounts.forms import UserLoginForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from accounts.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm#, ContactForm

def register(request):
    articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #if request.POST.get('section'):
                #form.section = request.POST.get('section')
            #form.save()
            username = form.cleaned_data.get('username')
            section = form.cleaned_data.get('section')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    context = {
        'title': 'Register',
        'articles': articles,
        'form': form,
    }

    return render(request, 'accounts/register.html', context)

class LoginView(auth_views.LoginView):
    def get_success_url(self):
        return resolve_url('main_website_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context['articles'] = articles
        context['title'] = 'Login'
        return context

class LogoutView(auth_views.LogoutView):
    def get_success_url(self):
        return resolve_url('logout')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context['articles'] = articles
        context['title'] = 'Logout'
        return context

@login_required
def profile(request):
    articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title': 'Profile',
        'articles': articles,
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'accounts/profile.html', context)