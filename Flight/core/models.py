import datetime

from django.db import models

class Dest(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    name = models.CharField(max_length=50)
    is_site = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Facts(models.Model):
    dest_name = models.ForeignKey(Dest, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    num_seat = models.DecimalField(max_digits=4, decimal_places=0)


    def __str__(self):
        return self.dest_name