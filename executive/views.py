from django.views import generic
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from main_website.models import Article
from django.core.exceptions import PermissionDenied
from executive.models import QuartermastersItemInventory
from django.contrib.auth.mixins import LoginRequiredMixin
from executive.forms import QuartermastersItemInventoryForm
from django.views.generic.edit import UpdateView, DeleteView

class ExecutiveIndexView(generic.View, LoginRequiredMixin):
    def get(self, request):
        if not request.user.is_staff or not request.user.is_superuser:
            raise PermissionDenied
        else:
            articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
            context = {
                'title': 'Home',
                'articles': articles
            }
            return render(request, 'executive/home.html', context)

class QuartermastersDatabaseView(generic.View, LoginRequiredMixin):
    def get(self, request):
        if not request.user.is_staff or not request.user.is_superuser:
            raise PermissionDenied
        else:
            articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
            queryset = QuartermastersItemInventory.objects.all()
            context = {
                'title': 'Home',
                'articles': articles,
                'queryset': queryset
            }
            return render(request, 'executive/quartermaster_database.html', context)

class QuartermastersDatabaseEditView(LoginRequiredMixin, UpdateView):
    model = QuartermastersItemInventory
    template_name = 'executive/database_item_edit.html'  # <app>/<model>_<viewtype>.html
    form_class = QuartermastersItemInventoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context['articles'] = articles
        context['title'] = 'Update Item'
        return context

class QuartermastersDatabaseDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('executive_quartermaster_database')
    model = QuartermastersItemInventory
    template_name = 'executive/database_item_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context['articles'] = articles
        context['title'] = 'Update Item'
        return context