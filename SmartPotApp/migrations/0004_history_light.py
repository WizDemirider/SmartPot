# Generated by Django 4.2.6 on 2023-12-03 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartPotApp', '0003_remove_history_humidity'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='light',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True),
        ),
    ]
