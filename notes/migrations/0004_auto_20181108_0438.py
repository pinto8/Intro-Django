# Generated by Django 2.1.3 on 2018-11-08 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20181108_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
