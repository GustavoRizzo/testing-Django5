from django.db import models
from django.db.models import F
from django.db.models.functions import Now, Pi
from django.utils import timezone


# Database-computed default values
class MyDeafultFieldModel(models.Model):
    age = models.IntegerField(db_default=18, default=17)
    created = models.DateTimeField(db_default=Now(), default=timezone.now)
    circumference = models.FloatField(db_default=2 * Pi())


# Database generated model fields
class Square(models.Model):
    side = models.IntegerField()
    area = models.GeneratedField(
        expression=F("side") * F("side"),
        output_field=models.BigIntegerField(),
        db_persist=True,
    )
