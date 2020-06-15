from django.contrib import admin
from . models import Customer


admin.site.site_header = 'CrosCrowd Creative'
admin.site.index_title = 'Admin'
admin.site.site_title = 'CrosCrowd Creative'


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


admin.site.register(Customer, CustomerAdmin)