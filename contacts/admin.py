from django.contrib import admin

from .models import ContactRequest



class ContactRequestAdmin(admin.ModelAdmin):

    list_display = ('user', 'name', 'company_name', 'email', 'read',)


admin.site.register(ContactRequest, ContactRequestAdmin)
