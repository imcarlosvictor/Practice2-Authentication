from django.db import models


# Create your models here.
class Accounts(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
