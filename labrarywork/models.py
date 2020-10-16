from django.db import models
from django.utils.timezone import timezone

# Create your models here.


class Category(models.Model):
    cat_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Book(models.Model):
    book_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    isbn = models.IntegerField()
    qty = models.IntegerField()


    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key = True)
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    classes = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.EmailField()
    datetime = models.DateTimeField(auto_now_add = True)
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.name
