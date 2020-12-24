from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

        
class College(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    university = models.ForeignKey(University, related_name='college_set', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    publisher_name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='book_set', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True)
    standard = models.PositiveIntegerField()
    books = models.ManyToManyField(Book, related_name='student_set', through="BookIssued")
    college = models.ForeignKey(College, related_name='student_set', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name        


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='library_set')
    total = models.PositiveIntegerField()
    college = models.ForeignKey(College, related_name='library_set', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = [['name', 'college']]

    def __str__(self):
        return self.name


class BookIssued(models.Model):
    student = models.ForeignKey(Student, related_name='book_issued_set', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='book_issued_set', on_delete=models.CASCADE)
    book_issued_date = models.DateField()
    library = models.ForeignKey(Library, related_name='book_issued_set', on_delete=models.CASCADE)
    college = models.ForeignKey(College, related_name='book_issued_set', on_delete=models.CASCADE)

    class Meta:
        unique_together = [['library', 'book', 'student']]

    def __str__(self):
        return f"{self.college.name} - {self.library.name} - {self.student.name} - {self.book.name}"
