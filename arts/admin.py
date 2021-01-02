from django.contrib import admin
from .models import Events
from .models import participants
# Register your models here.
admin.site.register(Events)
admin.site.register(participants)
