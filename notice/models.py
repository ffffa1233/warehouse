from django.db import models

# Create your models here.
class NoticeItem(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    context = models.CharField(max_length=1000, null=True)
    date_input = models.CharField(max_length=50, null=True)
