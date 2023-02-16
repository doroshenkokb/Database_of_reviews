from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import User



class Review(models.Model):
    #title = models.ForeignKey(
        #Title, 
        #on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(
        User,
        default=None,
        on_delete=models.CASCADE, 
        related_name='reviews'
    )
    score = models.FloatField(validators=[
        MinValueValidator(1.0),
        MaxValueValidator(10.0)
    ])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text


class Comments(models.Model):
    #title = models.ForeignKey(
        #Title, 
        #on_delete=models.CASCADE)
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
