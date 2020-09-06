from django.db import models


class User(models.Model):

    class Meta:
        db_table = 'user'

    # blank: Form, null: DB
    name = models.CharField(max_length=30)
    email = models.CharField(unique=True)
    password = models.CharField()

    def __str__(self):
        return self.name

