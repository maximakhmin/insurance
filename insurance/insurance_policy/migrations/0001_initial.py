# Generated by Django 5.0 on 2023-12-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('payment', models.IntegerField()),
                ('description', models.CharField(max_length=511)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
