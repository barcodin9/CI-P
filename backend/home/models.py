from django.db import models

# Create your models here.

class Newsletter(models.Model):
    email = models.EmailField(max_length=254, unique=True)

    class Meta:
        db_table = 'merchandise_newsletter'