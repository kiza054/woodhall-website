from django.urls import path

from beavers import views
from beavers.views import (PostCreate, PostDelete, PostList, PostUpdate,
                           UserPostList)

urlpatterns = [
    path('', PostList.as_view(), name='beavers_blog_home'),
    path('about/', views.AboutView.as_view(), name='beavers_blog_about'),
    path('search/', views.SearchView.as_view(), name='beavers_blog_search'),
    path('file_upload/', views.upload, name='beavers_blog_file_upload'),
    path('downloads/', views.DownloadView.as_view(), name='beavers_blog_downloads'),
    path('badge_placement', views.BadgePlacementView.as_view(), name='beavers_blog_badge_placement'),
    path('user/<str:username>', UserPostList.as_view(), name='beavers_blog_user_posts'),
    path('post/new_post/', PostCreate.as_view(), name='beavers_blog_post_create'),
    path('post/<slug:slug>/like/', views.PostLikeView, name='beavers_blog_post_like'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name="beavers_blog_post_detail"),
    path('post/update/<slug:slug>/', PostUpdate.as_view(), name='beavers_blog_post_update'),
    path('post/delete/<slug:slug>/', PostDelete.as_view(), name='beavers_blog_post_delete'),
    #path('post/tag/<slug:slug>/', views.tagged, name="cubs_blog_post_tags"),
]