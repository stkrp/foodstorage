from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from utils.models.base import CreatedAtMixin, ModifiedAtMixin
from users.models import User
from photos.models import Photo


class Rating(CreatedAtMixin, ModifiedAtMixin):
    MIN_VALUE = 1
    MAX_VALUE = 10

    # TODO: Проверить работоспособность валидаторов
    value = models.IntegerField(
        validators=[MinValueValidator(MIN_VALUE), MaxValueValidator(MAX_VALUE)]
    )
    user = models.ForeignKey(User, related_name='ratings')
    photo = models.ForeignKey(Photo, related_name='ratings')

    class Meta:
        unique_together = ('user', 'photo')
        ordering = ['-created_at']
