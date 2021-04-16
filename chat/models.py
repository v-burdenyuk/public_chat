from django.core.validators import MaxLengthValidator
from django.db import models


class Message(models.Model):
    email = models.EmailField()
    creation_date = models.DateTimeField(auto_now_add = True, editable = False)
    update_date = models.DateTimeField(auto_now = True, editable = False)
    text = models.TextField(validators = [MaxLengthValidator(100), ])

    def __str__(self):
        return self.text
