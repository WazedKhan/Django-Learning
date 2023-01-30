from rest_framework.generics import ListCreateAPIView

from post.serializers import PostListSerializer

from post.models import Post


class PostListVIew(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
