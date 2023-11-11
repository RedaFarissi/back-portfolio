from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ["title", "email", "message"]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Contact , ContactAdmin)