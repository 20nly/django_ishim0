from django.test import TestCase

from email.policy import default
from django.conf import settings
from django.db import models
from ishim import settings
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from models import CreateVacancy, CreateResume


# class Language:
#     language = models.CharField(
#         max_length = 50, choices=[
#             ('eng','английский'),('rus','русский'), ('tur', 'туркменский')
#             ], default='eng', verbose_name='Владение языками')
#     vacancy = models.ForeignKey(CreateVacancy, on_delete=models.CASCADE)
#     resume = models.ForeignKey(CreateResume, on_delete=models.CASCADE)
# class LanguageLevel:    
#     level = models.IntegerField(choices=[
#             (0,'не владею'),(1,'элементарный'), (3, 'ниже среднего')
#             ], default=0, null=True, blank=True,)
#     vacancy = models.ForeignKey(CreateVacancy, on_delete=models.CASCADE)
#     resume = models.ForeignKey(CreateResume, on_delete=models.CASCADE)