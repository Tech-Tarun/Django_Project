from django.db import models

class Details(models.Model):
    user = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pas = models.CharField(max_length=50)
    passcon = models.CharField(max_length=50)
    add = models.CharField(max_length=100)
    add1 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)

    def __str__(self):
        return self.user
