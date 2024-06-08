
from django.db import models
from users.models import User
from categories.models import Category
# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title