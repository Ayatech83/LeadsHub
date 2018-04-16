from django.db import models

class tender(models.Model):
    buyersName = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)
    refNum = models.CharField(max_length=100)
    issueDate = models.CharField(max_length=50)
    closingDate = models.CharField(max_length=50)
    siteInspection = models.TextField()
    description = models.TextField()


class category(models.Model):
    catCode = models.IntegerField(blank=False)
    catDescription = models.CharField(max_length=100)


class provinces(models.Model):
    provinceName = models.CharField(max_length=200)
