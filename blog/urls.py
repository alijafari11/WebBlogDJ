from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('test-page/', views.test, name='test'),
    path('post-list/', views.post_list, name='post-list'),
    path('post-list/<slug:tag_slug>/', views.post_list, name='post-list-tag'),
    # path('post-list/', views.PostListView.as_view(), name='post-list'),
    path('post-detail/<slug:slug>/<int:pk>/', views.post_detail, name='post-detail'),
    path('account-form/', views.user_account, name='account-form'),
    path('contact-us/', views.contactus, name='contact-us'),
    path('share-post/<int:post_id>/', views.share_post, name='share-post'),
]


