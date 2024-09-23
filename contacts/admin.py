from django.contrib import admin

from .models import ContactRequest, ContactEmailList



class ContactRequestAdmin(admin.ModelAdmin):

    list_display = ('name', 'company_name', 'email', 'read',)


class ContactEmailListAdmin(admin.ModelAdmin):

    list_display = ('name', 'company_name', 'email', 'is_user',)


admin.site.register(ContactRequest, ContactRequestAdmin)
admin.site.register(ContactEmailList, ContactEmailListAdmin)