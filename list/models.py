from django.db import models

# Create your models here.


class shoppingItem(models.Model):
    name = models.CharField(max_length=30, blank=False)
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return self.name