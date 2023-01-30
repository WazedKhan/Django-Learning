from django.urls import path
from post.views import PostListVIew

urlpatterns = [path("", PostListVIew.as_view(), name="post-list")]
