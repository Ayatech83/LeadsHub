from django.db import models

# Create your models here.

class Company(models.Model):
    comp_name = models.CharField(max_length=200)
    comp_reg_num = models.CharField(max_length=20)
    comp_addr = models.TextField()
    comp_vat = models.CharField(max_length=20)
    cont_person_title = models.CharField(max_length=7)
    cont_person_name = models.CharField(max_length=20)
    cont_person_surname = models.CharField(max_length=20)
    cont_person_number = models.CharField(max_length=20)
    cont_person_email = models.CharField(max_length=100)


