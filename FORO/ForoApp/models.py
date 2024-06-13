from django.db import models

class User(models.Model):
    username = models.CharField(max_length=55)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=100)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Post(models.Model):
    content = models.TextField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    thread= models.ForeignKey(Thread, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (self.user.username + " - " + self.thread.title)

