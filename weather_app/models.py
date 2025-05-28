from django.db import models


class SearchHistory(models.Model):
    city = models.CharField(max_length=100, verbose_name="Город")
    searched_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата последнего поиска")
    session_key = models.CharField(max_length=40, verbose_name="Сессионный ключ")

    def __str__(self):
        return f"{self.city} @ {self.searched_at}"
