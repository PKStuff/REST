from django.db import models

class employee(models.Model):

    name = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=20,default='7276637363')

    def __str__(self):
        return self.name+' '+self.lname
