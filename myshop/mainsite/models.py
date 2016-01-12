from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils import timezone
# import string
# import random
# from pyuploadcare.dj import ImageField

# Create your models here.

class Item(models.Model):
    title = models.CharField(validators = [validators.MinLengthValidator(2)], max_length = 75)
    text = models.TextField(validators = [validators.MinLengthValidator(50), validators.MaxLengthValidator(500)])#max_length = 200)
    price = models.FloatField(default = 0, validators = [validators.MinValueValidator(0)])
    photo = models.URLField(blank=True, validators = [validators.MinLengthValidator(8), validators.URLValidator], max_length = 200)
    # photos = models.ImageField(upload_to='pics/%Y/%m/%d', default='media/pics/no_image.png')
    # photos = models.FileField()
    email = models.CharField(validators = [validators.validate_email], max_length = 100)
    number = models.CharField(validators=[validators.RegexValidator(regex=r'^\+?1?\d{9,15}$')], max_length = 16)
    name = models.CharField(validators = [validators.MinLengthValidator(1)], max_length = 25)
    pub_date = models.DateTimeField(blank=True, null=True)
    categoriesChoice = (
        ('es', 'Estate'),
        ('tr', 'Transport'),
        ('el', 'Electronics'),
        ('st', 'Stuff'),
        ('ser', 'Services'),
        (None, ''),
        )
    category = models.CharField(max_length = 15, choices = categoriesChoice, default = None)
    vip = models.BooleanField(default = False)

    def __str__(self):
        return self.title
    def publishItem(self):
        self.pub_date = timezone.now()
        self.save()