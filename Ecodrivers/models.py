from django.db import models


class Starter(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Table(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now=True)
    # persons = models.IntegerField()
    message = models.TextField()

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
        db_table = 'Eco_Drivers'

    def __str__(self) -> str:
        return self.email

