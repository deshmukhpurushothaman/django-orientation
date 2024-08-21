from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=200)
    is_bestselling = models.BooleanField(default=False)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    # genre = models.CharField(max_length=200)
    # publication_date = models.DateField()
    # description = models.TextField()
    # image = models.ImageField(upload_to='book_images/')

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])

    def __str__(self):
        return f"{self.title} ({self.rating})"
