from django.db import models

class Dest(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=50)
    is_site = models.BooleanField()

    def __str__(self):
        return self.name



class Facts(models.Model):
    dest = models.ForeignKey(Dest, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.dest