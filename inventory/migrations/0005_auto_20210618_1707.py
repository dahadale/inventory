# Generated by Django 3.2.4 on 2021-06-18 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20210618_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='exit',
            name='date',
            field=models.DateField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exit',
            name='observations',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exit',
            name='owner',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.owner'),
            preserve_default=False,
        ),
    ]
