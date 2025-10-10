from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique = True)
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    operating_days = models.CharField(
        max_length=100,
        help_text="Enter days separated by commas (e.g., Mon, Tue, Wed, Thu, Fri"
    )

    def __str__(self):
        return self.name