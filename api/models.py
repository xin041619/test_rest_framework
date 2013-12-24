from django.db import models


class Set(models.Model):
    set_id = models.AutoField(primary_key=True)
    pub_date = models.DateTimeField('date published')


class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

class CardAndSetMap(models.Model):
    id = models.AutoField(primary_key=True)
    set_id = models.ForeignKey(Set)
    card_id = models.ForeignKey(Card)
    
