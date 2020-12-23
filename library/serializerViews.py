from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated, IsAuthenticatedOrReadOnly, 
                                        IsAdminUser, AllowAny)
from rest_framework.response import Response
from library.serializer import (AuthorInfoSerializer, BookInfoSerializer, StudentInfoSerializer,
                                BookIssuedInfoSerializer, LibraryInfoSerializer, CollegeInfoSerializer,
                                UniversityInfoSerializer)
from .models import Author, Book, Student, BookIssued, Library, College, University

class AuthorInfoView(viewsets.ModelViewSet):                
    serializer_class = AuthorInfoSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Author.objects.all()
        return queryset

class BookInfoView(viewsets.ModelViewSet):
    serializer_class = BookInfoSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Book.objects.all().select_related('author')
        return queryset

class StudentInfoView(viewsets.ModelViewSet):
    serializer_class = StudentInfoSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Student.objects.all().prefetch_related('books')
        return queryset

class BookIssuedInfoView(viewsets.ModelViewSet):
    serializer_class = BookIssuedInfoSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = BookIssued.objects.all().select_related('library', 'student', 'book')
        return queryset

class LibraryInfoView(viewsets.ModelViewSet):
    serializer_class = LibraryInfoSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Library.objects.all().prefetch_related('books')
        return queryset

class CollegeInfoView(viewsets.ModelViewSet):
    serializer_class = CollegeInfoSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = College.objects.all().select_related('library', 'student')
        return queryset

class UniversityInfoView(viewsets.ModelViewSet):
    serializer_class = UniversityInfoSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = University.objects.all().select_related('college')
        return queryset

#############################################################################
# IsAuthenticated: only authorised person can do anything
# IsAuthenticatedOrReadOnly: any user can read, but change by authorised user
# IsAdminUser: Only AdminUser
# AllowAny: Any user can access
#############################################################################
