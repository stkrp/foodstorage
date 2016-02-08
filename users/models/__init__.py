from django.db.models.signals import post_save

from .objects import User
from .signals import user_saved


post_save.connect(user_saved, User)
