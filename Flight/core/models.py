from django.db import models

class Facts(models.Model):
    dest = models.CharField(max_length=50)
    facts = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.dest