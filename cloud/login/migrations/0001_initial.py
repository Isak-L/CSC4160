# Generated by Django 2.1.7 on 2019-11-29 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('dID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('dAccount', models.CharField(blank=True, max_length=15)),
                ('dPassword', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
