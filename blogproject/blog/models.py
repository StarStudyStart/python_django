from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    
    title = models.CharField(max_length=100)
    body = models.TextField()
    
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    
    excerpt = models.CharField(max_length=200,blank = True)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank = True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    #自定义get_absolute_url
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs = {'pk':self.pk})
        
    class Meta:
        ordering = ['-create_time','title']
        
        
