# Generated by Django 3.2.4 on 2021-06-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_rename_date_requisition_date_requisition'),
    ]

    operations = [
        migrations.AddField(
            model_name='exit',
            name='purchase_order',
            field=models.CharField(default=-131, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exit',
            name='observations',
            field=models.TextField(max_length=250),
        ),
    ]