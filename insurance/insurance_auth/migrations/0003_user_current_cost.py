# Generated by Django 5.0 on 2023-12-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_auth', '0002_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='current_cost',
            field=models.IntegerField(default=None),
        ),
    ]
