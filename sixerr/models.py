from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=500)
    about = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.username


class Gig(models.Model):
    CATEGORY_CHOICES = (
        ('GD', 'Графика и Дизайн'),
        ('MR', 'Маркетинг'),
        ('VD', 'Видеообработка'),
        ('MA', 'Музыка и Аудио'),
        ('IT', 'ИТ')
    )
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(default=5)
    photo = models.FileField(upload_to='gigs')
    status = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
