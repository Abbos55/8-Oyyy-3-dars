from rest_framework import generics
from .models import Genre, Book
from .serializers import GenreSerializer, BookSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        janrlar = Genre.objects.all()
        return janrlar

    def get_serializer_class(self):
        return GenreSerializer

class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    lookup_url = 'id'

    def get_queryset(self):
        janrlar = Genre.objects.all()
        return janrlar

    def get_serializer_class(self):
        return GenreSerializer

class BookListCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        kitoblar = Book.objects.all()
        return kitoblar

    def get_serializer_class(self):
        return BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    lookup_url = 'id'

    def get_queryset(self):
        kitoblar = Book.objects.all()
        return kitoblar

    def get_serializer_class(self):
        return BookSerializer
