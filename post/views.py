from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from post.serializers import PostListSerializer, QRSerializer

from post.models import Post

from core.models import QR

class PostListVIew(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]

import qrcode

class PostQR(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request, format=None, **kwargs):
        request.data['name'] = "Hey"
        serializer = QRSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)