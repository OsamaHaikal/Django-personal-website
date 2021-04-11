from django.contrib import admin
from .models import Skill,Portfolio,Contact

admin.site.register(Skill)

admin.site.register(Portfolio)


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email', 'message')
