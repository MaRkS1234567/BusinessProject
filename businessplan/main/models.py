from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Review(models.Model):
    task = models.TextField('Reviews')
    stars = models.PositiveSmallIntegerField('Stars', validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.task

    def stars_range(self):
        """ Used in templates to render self.stars number of stars """
        return range(self.stars)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='valid_stars_range',
                check=models.Q(stars__gt=0) & models.Q(stars__lt=6)
            ),
        ]

