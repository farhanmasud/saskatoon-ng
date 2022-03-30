# Generated by Django 3.2.5 on 2021-09-11 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvest', '0005_auto_20210818_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='shared',
            field=models.BooleanField(default=False, help_text='Can be used in harvests outside of property', verbose_name='Shared'),
        ),
    ]
