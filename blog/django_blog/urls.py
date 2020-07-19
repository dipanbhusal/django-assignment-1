from django.urls import path
from .views import BlogHome, PostCreate, PostDetail, PostUpdate, PostDelete
urlpatterns = [
    path('' , BlogHome.as_view(), name = 'blog-home'),
    path('create/', PostCreate.as_view(), name = 'post-create'),
    path('post/<slug:slug>/', PostDetail.as_view(), name = 'post-detail'),
    path('post/<slug:slug>/update/', PostUpdate.as_view(), name = 'post-update'),
    path('post/<slug:slug>/delete/', PostDelete.as_view(), name = 'post-delete'),
]