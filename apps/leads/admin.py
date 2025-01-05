from django.contrib import admin
from apps.leads.models import User, Lead, Agent, UserProfile

# Register your models here.
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(UserProfile)
