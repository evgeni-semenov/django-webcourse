# Generated by Django 4.2.1 on 2023-05-26 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0004_tasting'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasting',
            name='drink',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasting', to='drinks.drink'),
        ),
    ]