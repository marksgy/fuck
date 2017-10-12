from django.db import models


class People(models.Model):
    id = models.CharField(max_length=32,primary_key=True)
    reply_channel= models.CharField(max_length=32)
    online=models.IntegerField(null=True)

class ChatMessage(models.Model):
    fromid=models.CharField(max_length=32,default="hey")
    toid=models.CharField(max_length=32,default="hey")
    text=models.CharField(max_length=128,default="hey")
    issent=models.IntegerField(null=True)