# Generated by Django 3.2.3 on 2021-06-23 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0005_alter_exit_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='user_requesting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]