from django.db import models

# Create your models here.
class Review(models.Model):
      sku = models.CharField(max_length=20)
      rating = models.IntegerField()
      title = models.CharField(max_length=120)
      author = models.CharField(max_length=20)
      text = models.TextField()
      source = models.CharField(max_length=20)

      def _str_(self):
        return self.title