from django.contrib import admin
from .models import Events
# # from .models import participants
from .models import registration
# Register your models here.

# admin.site.register(Events)
# # admin.site.register(participants)
admin.site.register(registration)

class ArtsAdmin(admin.ModelAdmin):
    list_display = ('event_name','event_venue',)
    search_fields=('event_name','event_venue',)
    class Meta:
        model = Events

admin.site.register(Events,ArtsAdmin)
