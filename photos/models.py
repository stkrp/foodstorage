from django.db import models
from utils.models import TitleMixin, CreatedAtMixin, ModifiedAtMixin
from users.models import User
from decimal import Decimal, ROUND_HALF_UP


class Photo(TitleMixin, CreatedAtMixin, ModifiedAtMixin):
    file = models.CharField(max_length=255)  # models.ImageField()
    user = models.ForeignKey(User, related_name='photos')

    class Meta:
        ordering = ['-created_at']

    def fetch_avg_rating(self, default=0):
        aggregate_dict = self.ratings.all().aggregate(models.Avg('value'))
        avg_rating = aggregate_dict.get('value__avg', None)
        if avg_rating is None:
            return default
        avg_rating = int(Decimal(avg_rating).to_integral_value(ROUND_HALF_UP))
        return avg_rating
