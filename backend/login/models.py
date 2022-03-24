import json
from django.db import models

class user(models.Model):
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    def __str__(self):
        return '\n'+json.dumps({'user': self.account, 'password': self.password}, indent=4)+'\n'
    
    