# Generated by Django 4.2.1 on 2023-05-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0002_drink_alcohol_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinktype',
            name='type_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
