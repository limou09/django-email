# Generated by Django 2.1 on 2019-06-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_cityinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityinfo',
            name='area_name',
            field=models.CharField(max_length=50),
        ),
    ]