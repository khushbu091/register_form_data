from django.db import models

# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=150)
    Email=models.EmailField()
    Password=models.IntegerField()
    City=models.CharField(max_length=150)

    class Meta:
        db_table='Register'
        verbose_name_plural='Register'

    def __str__(self):
        return self.Name
