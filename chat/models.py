from django.db import models


# Create your models here.

class message (models.Model):
    content = models.TextField(blank=True, null=True)
    group = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey("chat.user", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{0}: {1}".format(self.user, self.content)
    
class user (models.Model):
    name = models.CharField(max_length=50, null=True, blank= True)
    
    def __str__(self):
        return self.name
    