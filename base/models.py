from django.db import models

# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=50,null=True,blank=True)
    book_name = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    createdTime=models.DateTimeField(auto_now_add=True)
    # fields =['desc','price']
 
    def __str__(self):
           return self.book_name + " " + self.author