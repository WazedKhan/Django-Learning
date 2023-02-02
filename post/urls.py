from django.urls import path
from post.views import PostListVIew, PostQR

urlpatterns = [
    path("", PostListVIew.as_view(), name="post-list"),
    path("qr", PostQR.as_view(), name="qr")
]
