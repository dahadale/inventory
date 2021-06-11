# Generated by Django 3.2.4 on 2021-06-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_movement_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movement',
            name='date_shelflife',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movement',
            name='lot',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
