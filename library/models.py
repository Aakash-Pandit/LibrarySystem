from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True)

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
    
    def __str__(self):
        return self.name        


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='library_set')
    total = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name


class BookIssued(models.Model):
    library = models.ForeignKey(Library, related_name='bookIssued_set', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='bookIssued_set', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='bookIssued_set', on_delete=models.CASCADE)
    date_issued = models.DateField()

    class Meta:
        unique_together = [['library', 'book', 'student']]

    def __str__(self):
        return f"{self.library.name} - {self.student.name} - {self.book.name}"


class College(models.Model):
    name = models.CharField(max_length=100)
    library = models.ForeignKey(Library, related_name='college_set', on_delete=models.PROTECT)
    student = models.ForeignKey(Student, related_name='college_set', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, related_name='university_set', on_delete=models.PROTECT)

    def __str__(self):
        return self.name