# Generated by Django 3.1.2 on 2020-11-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_auto_20201029_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='career_average',
            field=models.FloatField(null=True),
        ),
    ]