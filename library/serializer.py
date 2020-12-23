from rest_framework import serializers 
from library.models import Author, Book, Student, BookIssued, Library, College, University

class AuthorInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'
        # depth = 0

class BookInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1

class StudentInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
        # depth = 2

class BookIssuedInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookIssued
        fields = '__all__'
        # depth = 3

class LibraryInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Library
        fields = '__all__'
        # depth = 2

class CollegeInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = '__all__'
        # depth = 3

class UniversityInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = '__all__'
        # depth = 4