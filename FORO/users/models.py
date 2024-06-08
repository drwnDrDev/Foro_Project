from django.db import models

class User(models.Model):
    username = models.CharField(max_length=55)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
