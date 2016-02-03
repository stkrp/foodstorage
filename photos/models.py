from django.db import models
from django.db.models import Prefetch
from utils.models.base import TitleMixin, CreatedAtMixin, ModifiedAtMixin
from utils.models.expressions import Round
from users.models import User


class Photo(TitleMixin, CreatedAtMixin, ModifiedAtMixin):
    _RATING_DECIMALS = 0

    file = models.CharField(max_length=255)  # models.ImageField()
    user = models.ForeignKey(User, related_name='photos')

    class Meta:
        ordering = ['-created_at']

    def fetch_avg_rating(self):
        aggregate_dict = self.ratings.all().aggregate(
            Round(models.Avg('value'), self._RATING_DECIMALS)
        )
        return aggregate_dict.get('value__avg', None)

    @property
    def avg_rating(self):
        """
        Средняя оценка фото

        Если средняя оценка не вычислена в запросе, то она будет получена
        отдельным запросом и закэширована.

        Пример вычисления средней оценки в запросе:
        qs.annotate(
            avg_rating=Round(
                models.Avg('ratings__value'), cls._RATING_DECIMALS
            )
        )
        :return:
        """
        if not hasattr(self, '_avg_rating'):
            self._avg_rating = self.fetch_avg_rating()
        return self._avg_rating

    @avg_rating.setter
    def avg_rating(self, value):
        self._avg_rating = value

    @avg_rating.deleter
    def avg_rating(self):
        del self._avg_rating

    @classmethod
    def all_with_avg_rating(cls):
        """
        Получает фотографии со средней оценкой одним запросом,
        вместо запроса на каждую фотографию.

        :return:
        """
        return cls.objects.all().annotate(
            avg_rating=Round(
                models.Avg('ratings__value'), cls._RATING_DECIMALS
            )
        )

    @classmethod
    def all_with_ratings_fetched(cls):
        return cls.objects.all().prefetch_related(
            Prefetch('ratings', to_attr='ratings_fetched')
        )
