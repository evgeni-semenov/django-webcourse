# Generated by Django 4.2.1 on 2023-05-26 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0003_alter_drinktype_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
