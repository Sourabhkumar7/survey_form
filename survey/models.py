from django.db import models

# Create your models here.
from django.db import models

class SurveyResponse(models.Model):
    question = models.CharField(max_length=255)
    response = models.IntegerField()
