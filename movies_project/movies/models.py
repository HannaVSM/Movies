from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        text = "{0} ({1}) - {2}"
        return text.format(self.title, self.country, self.rating)
