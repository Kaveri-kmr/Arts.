from django.contrib import admin
from .models import Events
from .models import participants
from .models import registration
# Register your models here.
admin.site.register(Events)
admin.site.register(participants)
admin.site.register(registration)
