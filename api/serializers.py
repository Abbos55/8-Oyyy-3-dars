from rest_framework import serializers
from .models import Genre, Book

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']
        read_only_fields = ['id']

class BookSerializer(serializers.ModelSerializer):
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        source='genre',
        write_only=True
    )

    class Meta:
        model = Book
        exclude = ['description']
        depth = 1
        read_only_fields = ['id']
        extra_kwargs = {
            'price': {'required': True}
        }
