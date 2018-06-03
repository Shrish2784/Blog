from django.urls import path
from Blogs import views


app_name = 'Blogs'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/user/', views.PostUserListView.as_view(), name='post_user_list'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/drafts/', views.DraftListView.as_view(), name='post_drafts_list'),
    path('post/<pk>/publish', views.post_publish, name='post_publish'),
    path('post/<pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<pk>/remove/', views.comment_remove, name='comment_remove'),
    path('about/', views.AboutView.as_view(), name='about'),
]
