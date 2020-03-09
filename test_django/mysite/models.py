from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state_province = models.CharField(max_length=64)
    website = models.URLField()

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True,null=True,verbose_name="e-mail")

    def __str__(self):
        return "%s %s" % (self.first_name,self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=128, verbose_name="书名")
    author = models.ManyToManyField(Author, verbose_name="作者")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name="出版商")
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
