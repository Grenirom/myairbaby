from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()


class New(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/news')
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name='rating')
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ], blank=True, null=True
    )


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name='comments')
