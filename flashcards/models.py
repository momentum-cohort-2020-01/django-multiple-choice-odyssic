from django.db import models
from django.utils.text import slugify
from datetime import datetime
from django.contrib.auth import get_user_model
from users.models import User


class Deck(models.Model):
    name = models.CharField(max_length=60)
    subject = models.CharField(max_length=60)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length = 300, default = 'Add a Description')
    user = models.ForeignKey(
        User, null=True, related_name='decks', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.subject}'


class Card(models.Model):

    deck = models.ForeignKey(
        'Deck', on_delete=models.CASCADE, default='', related_name='cards')
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.question} {self.answer}'


class Interval(models.Model):
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             related_name='intervals')
    deck = models.ForeignKey(to=Deck,
                             on_delete=models.CASCADE,
                             related_name='intervals')
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
