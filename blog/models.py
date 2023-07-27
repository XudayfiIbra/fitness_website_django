from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images')
    content = models.TextField()
    published = models.BooleanField(default=False)
    tags = models.CharField(max_length=30)
    created_by = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    # def __str__ (self):
    #     return self.title
    