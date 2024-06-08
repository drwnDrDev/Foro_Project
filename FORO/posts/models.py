from django.db import models
from users.models import User
from threads.models import Thread
class Post(models.Model):
    content = models.TextField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    thread= models.ForeignKey(Thread, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (self.user.username + " - " + self.thread.title)
