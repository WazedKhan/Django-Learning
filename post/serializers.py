from rest_framework.serializers import ModelSerializer

from post.models import Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content"]
