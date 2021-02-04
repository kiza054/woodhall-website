from scouts import views
from django.urls import path
from scouts.views import (
    PostList,
    PostCreate,
    PostUpdate,
    PostDelete,
    UserPostList
)

urlpatterns = [
    path('', PostList.as_view(), name='scouts_blog_home'),
    path('about/', views.AboutView.as_view(), name='scouts_blog_about'),
    path('search/', views.SearchView.as_view(), name='scouts_blog_search'),
    path('file_upload/', views.upload, name='scouts_blog_file_upload'),
    path('downloads/', views.DownloadView.as_view(), name='scouts_blog_downloads'),
    #path('badge_placement', views.BadgePlacementView.as_view(), name='scouts_blog_badge_placement'),
    path('user/<str:username>', UserPostList.as_view(), name='scouts_blog_user_posts'),
    path('post/new_post/', PostCreate.as_view(), name='scouts_blog_post_create'),
    path('post/<slug:slug>/', views.post_detail, name='scouts_blog_post_detail'),
    path('post/update/<slug:slug>/', PostUpdate.as_view(), name='scouts_blog_post_update'),
    path('post/delete/<slug:slug>/', PostDelete.as_view(), name='scouts_blog_post_delete'),
    #path('post/tag/<slug:slug>/', views.tagged, name='scouts_blog_post_tags'),
]