from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100, null=True)
    publisher_name = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    standard = models.PositiveIntegerField(null=True)
    book = models.ManyToManyField(Book, through="BookIssued")
    
    def __str__(self):
        return self.name        


class Library(models.Model):
    name = models.CharField(max_length=100, null=True)
    book = models.ManyToManyField(Book)
    total = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return self.name


class BookIssued(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    date_enrolled = models.DateField(null=True)

    class Meta:
        unique_together = [['library', 'book', 'student']]

    def __str__(self):
        return f"{self.library.name} - {self.student.name} - {self.book.name}"


class College(models.Model):
    name = models.CharField(max_length=100, null=True)
    library = models.ManyToManyField(Library)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=100, null=True)
    college = models.ManyToManyField(College)

    def __str__(self):
        return self.name