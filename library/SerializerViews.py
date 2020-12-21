from rest_framework import viewsets
from rest_framework.response import Response
from library.serializer import AuthorInfoSerializer, BookInfoSerializer, StudentInfoSerializer
from .models import Author, Book, Student, BookIssued

class AuthorInfoView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorInfoSerializer

class BookInfoView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookInfoSerializer

class StudentInfoView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentInfoSerializer
