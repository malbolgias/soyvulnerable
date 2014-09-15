from django.db import models

# Create your models here.

class vulnerable(models.Model):
  ip_add = models.CharField(max_length=20)
  hostname = models.CharField(max_length=50, default="")
  country = models.CharField(max_length=4, default="CO")
  city = models.CharField(max_length=30, default="")
  vulnerable = models.BooleanField(default=True)
  port = models.CharField(max_length=20)
  date = models.DateTimeField('Fecha de prueba')
  result = models.TextField(max_length=300, default="N/A")
  def __unicode__(self):
    return self.ip_add
  
