from django.contrib import admin

from .models import Business


class BusinessAdmin(admin.ModelAdmin):
    fields = ['ruc', 'business_name', 'address', 'phone',
              'legal_representative_name', 'legal_representative_dni']
    ordering = ('id',)


admin.site.register(Business, BusinessAdmin)
