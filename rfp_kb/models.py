from django.db import models


class rfp_bk(models.Model):
    # This class models the RFP questions and answers
    rfp_name = models.CharField(max_length=200)  #this will be a lookup field
    question = models.CharField(max_length=2048)
    topic = models.CharField(max_length=100)  #this will be a lookup field
    answer = models.CharField(max_length=2048)
    winLoss = models.BooleanField()
    comply = models.BooleanField()
    product = models.CharField(max_length=200, null=True ) #this will be a lookup field
    product_variant = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.question

class rfp(models.Model):
    rfp_name = models.CharField(max_length=200)
    customer = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    value = models.FloatField()
    question_id = models.ForeignKey(rfp_bk, on_delete=models.CASCADE)

    def __str__(self):
        return self.rfp_name

class product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=2000)

    def __str__(self):
        return self.product_name
