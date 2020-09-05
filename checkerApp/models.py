from django.db import models


# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=50, null=False, blank=False)
    partsOfSpeech = models.CharField(max_length=25, default="")
    meaning = models.CharField(max_length=500, null=False, blank=False, default="")

    class Meta:
        verbose_name_plural = 'Words'
    
    def __str__(self):
        return self.word
