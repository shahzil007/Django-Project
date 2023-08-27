from django.db import models

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
