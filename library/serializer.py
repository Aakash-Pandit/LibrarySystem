from rest_framework import serializers 
from library.models import Author, Book, Student

class AuthorInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'
        depth = 0

class BookInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
        depth = 1

class StudentInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
        depth = 2