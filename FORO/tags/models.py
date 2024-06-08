from django.db import models

class Tag(models.Model):            # <--- Tag model
    tag_name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name