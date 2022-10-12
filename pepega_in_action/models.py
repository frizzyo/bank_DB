from django.db import models

# Create your models here.
class Frog(models.Model):
    colour = (
        ('g', 'green'),
        ('b', 'blue'),
    )
    name = models.CharField(max_length=30, primary_key=True)
    color = models.CharField(max_length=1, choices=colour)
    age = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

class Memes(models.Model):
    name = models.ForeignKey(Frog, on_delete=models.CASCADE)
    release_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name