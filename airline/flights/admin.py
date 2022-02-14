from django.contrib import admin

# Register your models here.
from .models import Flight, Airport, Passengers

class FlightAdmin(admin.ModelAdmin):
    list_display=("id","origin","destination","duration")

class PassengersAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passengers, PassengersAdmin)