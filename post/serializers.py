from rest_framework.serializers import ModelSerializer

from post.models import Post
from core.models import QR


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content"]

class QRSerializer(ModelSerializer):
    class Meta:
        model = QR
        fields = ["qr_code", "name"]
        write_only_fields = ["name"]
        read_only_fields = ["qr_code"]