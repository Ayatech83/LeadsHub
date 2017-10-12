from django.db import models

# Create your models here.

class Company(models.Model):
    comp_name = models.CharField(max_length=200)
    comp_reg_num = models.CharField(max_length=20)
    comp_addr = models.TextField()
    comp_vat = models.CharField(max_length=20)


