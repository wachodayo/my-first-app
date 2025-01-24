from django.db import models

class User(models.Model):
    GENDER_CHOICES = [
        ('m', 'Male'),
        ('f', 'Female'),
    ]

    PURPOSE_CHOICES = [
        ('f', 'Friend'),
        ('l', 'Lover'),
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='m')  # デフォルト値を設定
    age = models.IntegerField(default=0)  # デフォルト値を設定
    purpose = models.CharField(max_length=1, choices=PURPOSE_CHOICES, default='f')  # デフォルト値を設定
    opp_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='f')  # デフォルト値を設定
    opp_age = models.IntegerField(default=25)
    personality_1 = models.CharField(max_length=1, default='e')  # デフォルト値を設定
    personality_2 = models.CharField(max_length=1, default='e')  # デフォルト値を設定
    hobby_1 = models.CharField(max_length=1, default='e')  # デフォルト値を設定
    hobby_2 = models.CharField(max_length=1, default='e')  # デフォルト値を設定
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name