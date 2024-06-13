from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=55)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Nombre: {self.username}, Mail: {self.email}'


# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=100)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Titulo: {self.title} , Creado por: {self.user}'

class Post(models.Model):
    content = models.TextField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    thread= models.ForeignKey(Thread, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Usuario: {self.user}, Post en: {self.created_at}'

class Votes(models.Model):
    TYPE_CHOICE= {
        ("CO", "Confirmo"),
        ("NO", "No me parece"),
    }
    vote_type = models.CharField(max_length=20, choices=TYPE_CHOICE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Voto: {self.user} Type: {self.vote_type}'