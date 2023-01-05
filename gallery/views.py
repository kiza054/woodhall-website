from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import generic

from gallery.forms import AddImageCategoryForm, UploadImageForm
from gallery.models import ImageGallery, ImageGalleryCategory
from main_website.models import Article


class ImageGalleryView(LoginRequiredMixin, generic.View):
    def get(self, request):
        articles = Article.objects.filter(status=1).order_by('-date_posted')[:2]
        category = request.GET.get('category')
        if category == None:
            images = ImageGallery.objects.all()
        else:
            images = ImageGallery.objects.filter(category__name=category)

        categories = ImageGalleryCategory.objects.all()
        context = {
            'images': images,
            'articles': articles,
            'categories': categories,
            'title': 'Image Gallery'
        }
        return render(request, 'gallery/image_gallery.html', context)

class ImageDetailView(LoginRequiredMixin, generic.View):
    def get(self, request, pk):
        images = ImageGallery.objects.get(id=pk)
        context = {
            'images': images,
            'title': 'Image Details'
        }
        return render(request, 'gallery/image_detail.html', context)

class ImageAddView(LoginRequiredMixin, generic.View):
    def get(self, request):
        form = UploadImageForm()
        context = {
            'form': form,
            'title': 'Add Image'
        }
        return render(request, 'gallery/image_upload.html', context)

    def post(self, request):
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image Successfully Uploaded')
            return redirect('gallery')

class ImageCategoryAddView(LoginRequiredMixin, generic.View):
    def get(self, request):
        form = AddImageCategoryForm()
        context = {
            'form': form,
            'title': 'Add Category'
        }
        return render(request, 'gallery/image_add_category.html', context)

    def post(self, request):
        form = AddImageCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Successfully Added')
            return redirect('gallery')