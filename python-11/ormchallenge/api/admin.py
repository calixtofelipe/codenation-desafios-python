from django.contrib import admin
from api.models import User, Agent, Event, Group 
# Register your models here.
admin.site.register(Group)
admin.site.register(Agent)
admin.site.register(Event)
admin.site.register(User)