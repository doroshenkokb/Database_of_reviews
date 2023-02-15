from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    title = models.IntegerField()  # Потом свяжем с произведениями
    text = models.TextField()
    #author = models.ForeignKey(
        #User, on_delete=models.CASCADE, related_name='reviews')
    score = models.FloatField(validators=[
        MinValueValidator(1.0),
        MaxValueValidator(10.0)
    ])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text

