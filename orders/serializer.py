from rest_framework.serializers import ModelSerializer

from core.models import Order, Product, Track, Album


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price"]


class OrderSerializer(ModelSerializer):
    # product = ProductSerializer()
    class Meta:
        model = Order
        fields = ["product", "customer"]


class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']


class AlbumSerializer(ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album

