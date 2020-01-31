from django.contrib import admin
from emailsender.models import Email


@admin.register(Email)
class AdminEmail(admin.ModelAdmin):
    pass
