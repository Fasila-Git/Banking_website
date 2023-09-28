from django.db import models


# Create your models here.
class BankForm(models.Model):
    Name = models.CharField(max_length=20)
    DOB = models.DateField()
    Age = models.DecimalField(max_digits=3, decimal_places=3)
    Phone = models.IntegerField()
    Address = models.TextField(max_length=250)
    Gender = models.CharField(max_length=20)
    Email = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    Branch = models.CharField(max_length=100)
    Credit_card = models.CharField(max_length=20)
    Materials=models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class AllDist(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='district'
        verbose_name_plural='districts'


    def __str__(self):
        return self.name

class AllBranch(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)
    district=models.ForeignKey(AllDist,on_delete=models.CASCADE)

    class Meta:
        ordering=('name',)
        verbose_name='branch'
        verbose_name_plural='branches'

    def __str__(self):
        return self.name
