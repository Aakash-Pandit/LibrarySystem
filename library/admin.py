from django.contrib import admin
from .models import Author, Book, Student, BookIssued, Library, College, University

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(BookIssued)
admin.site.register(Library)
admin.site.register(College)
admin.site.register(University)