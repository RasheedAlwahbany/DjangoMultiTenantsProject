# Generated by Django 4.2.1 on 2023-05-30 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenantawaremodel',
            name='tenant',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Tenant',
        ),
        migrations.DeleteModel(
            name='TenantAwareModel',
        ),
    ]
