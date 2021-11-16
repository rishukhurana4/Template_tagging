from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def _str_(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def _str_(self):
        return self.name

class AccessRecords(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.PROTECT)
    date = models.DateField()

    def _str_(self):
        return str(self.date)
