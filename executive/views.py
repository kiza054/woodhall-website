from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from executive.forms import QuartermastersItemInventoryForm
from executive.models import QuartermastersItemInventory
from main_website.models import Article


class ExecutiveIndexView(generic.View, LoginRequiredMixin):
    def get(self, request):
        if request.user.is_executive or request.user.is_superuser:
            articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
            context = {
                'title': 'Home',
                'articles': articles
            }
            return render(request, 'executive/home.html', context)
        else:
            raise PermissionDenied

class QuartermastersDatabaseView(generic.View, LoginRequiredMixin):
    def get(self, request):
        if request.user.is_executive or request.user.is_superuser:
            articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
            queryset = QuartermastersItemInventory.objects.all()
            context = {
                'title': 'Home',
                'articles': articles,
                'queryset': queryset
            }
            return render(request, 'executive/quartermaster_database.html', context)
        else:
            raise PermissionDenied

class QuartermastersDatabaseAddView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('executive_quartermaster_database')
    model = QuartermastersItemInventory
    template_name = 'executive/database_item_add.html'  # <app>/<model>_<viewtype>.html
    form_class = QuartermastersItemInventoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        context['articles'] = articles
        context['title'] = 'Add Item'
        return context

class QuartermastersDatabaseEditView(LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy('executive_quartermaster_database')
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
        context['title'] = 'Delete Item'
        return context