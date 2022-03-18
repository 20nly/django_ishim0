from django.contrib import admin

# Register your models here.
from .models import CreateVacancy
from .models import CreateResume

admin.site.register(CreateVacancy)
admin.site.register(CreateResume)