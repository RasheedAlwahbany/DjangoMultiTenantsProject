from django.contrib import admin
from .models import Domain, Tenant
# Register your models here.

admin.site.register(Tenant)
admin.site.register(Domain)

