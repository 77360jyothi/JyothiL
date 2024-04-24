from django.contrib import admin
from .models import Place, TeamMember  # Check if the correct file path is used for models

# Register your models here.
admin.site.register(Place)
admin.site.register(TeamMember)
