# Generated by Django 3.2.4 on 2021-06-08 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.CharField(max_length=50)),
                ('item_name', models.CharField(max_length=100)),
                ('fsc', models.CharField(max_length=10)),
                ('niin', models.CharField(max_length=20)),
                ('unit_price', models.FloatField()),
                ('unit_issue', models.CharField(max_length=10)),
                ('shelf_life', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_type', models.CharField(choices=[('entry', 'Entrada'), ('exit', 'Salida')], default='exit', max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('course', models.CharField(max_length=100)),
                ('purchase_order', models.CharField(max_length=10)),
                ('lot', models.CharField(max_length=20)),
                ('date_shelflife', models.DateField()),
                ('quantity', models.IntegerField()),
                ('user_requesting', models.CharField(max_length=20)),
                ('user_deliver', models.CharField(max_length=20)),
                ('login_user', models.CharField(max_length=20)),
                ('count', models.IntegerField()),
                ('consumable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.consumable')),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Location_consumable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.consumable')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.location')),
            ],
        ),
    ]
