# Generated by Django 2.2 on 2019-04-24 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmovements', '0005_auto_20190424_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhead',
            name='SNo',
            field=models.IntegerField(),
        ),
    ]
