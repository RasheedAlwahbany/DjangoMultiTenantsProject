from django.db import models
from django.contrib.auth.models import User
from django_tenants.models import DomainMixin, TenantMixin
# Create your models here.
class Tenant(TenantMixin):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    updated_at = models.DateTimeField(auto_now=True, null=True)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=False, blank=True)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and
    # synced when it is saved
    auto_create_schema = True

    """
    USE THIS WITH CAUTION!
    Set this flag to true on a parent class if you want the schema to be
    automatically deleted if the tenant row gets deleted.
    """
    auto_drop_schema = True


    def __str__(self):
        return f"{self.schema_name}"
    
class Domain(DomainMixin):
    pass