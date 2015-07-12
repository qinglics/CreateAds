from django.db import models

# Create your models here.

class Ad(models.Model):
    ad_id = models.CharField(max_length = 100)
    ad_title = models.TextField()
    ad_text = models.TextField()
    ad_pics = models.TextField()
    others = models.TextField()
    
    def __str__(self):
        return self.ad_title