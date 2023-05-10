from django.db import models


class rfp_bk(models.Model):
    rfp_name = models.CharField(max_length=200)  #this will be a lookup field
    question = models.CharField(max_length=2048)
    topic = models.CharField(max_length=100)  #this will be a lookup field
    answer = models.CharField(max_length=2048)
    winLoss = models.BooleanField()
    comply = models.BooleanField()

    def __str__(self):
        return self.question
