from django.db import models

class articles(models.Model):
    title = models.CharField(max_length=300)
    articleBody = models.TextField()
    publisher = models.CharField(max_length=100)

