from django.db import models
from django.urls import reverse
# Create your models here.

# class MyModelName(models.Model):
#     my_field_name = models.CharField(
#         max_length=20,
#         help_text='Enter field documentation',
#     )

#     class Meta:
#         ordering = ['-my_field_name']
#         #ordering = ['title', '-pubdate']

#     def get_absolute_url(self):
#         return reverse('model-detail-view', args=[str(self.id)])

#     def __str__(self):
#         return self.my_field_name


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Enter a book genre (e.g. Science Fiction)'
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        null=True,
    )
    summary = models.TextField(
        max_length=1000,
        help_text='Enter a brief description of the book',
    )
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        unique=True,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
        )
    genre = models.ManyToManyField(
        Genre,
        help_text='Select a genre for this book',
        )
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
