from django.db import models
import datetime
# Create your models here.
class Notes(models.Model):
    title=models.CharField(max_length=300)
    paragraph1=models.CharField(max_length=10000,null=True)
    paragraph2=models.CharField(max_length=10000,null=True)
    paragraph3=models.CharField(max_length=10000,null=True)
    paragraph4=models.CharField(max_length=10000,null=True)
    paragraph5=models.CharField(max_length=10000,null=True)
    paragraph6=models.CharField(max_length=10000,null=True)
    paragraph7=models.CharField(max_length=10000,null=True)
    paragraph8=models.CharField(max_length=10000,null=True)
    paragraph9=models.CharField(max_length=10000,null=True)
    paragraph10=models.CharField(max_length=10000,null=True)
    date_created=models.DateTimeField(auto_created=True,default=datetime.datetime.now())
