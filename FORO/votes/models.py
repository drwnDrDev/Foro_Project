from django.db import models
from users.models import User
from threads.models import Thread

class Vote(models.Model):            # <--- Vote model
    vote = models.BooleanField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    thread= models.ForeignKey(Thread, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vote