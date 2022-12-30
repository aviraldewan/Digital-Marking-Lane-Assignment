from django.db import models

# Likes Class
class Likes(models.Model):
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.likes}"

# Dislikes Class
class Dislikes(models.Model):
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.dislikes}"
