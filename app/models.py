from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    purpose = models.CharField(max_length=1)
    opp_gender = models.CharField(max_length=1)
    opp_age = models.IntegerField()
    personality_1 = models.CharField(max_length=1)
    personality_2 = models.CharField(max_length=1)
    hobby_1 = models.CharField(max_length=1)
    hobby_2 = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name