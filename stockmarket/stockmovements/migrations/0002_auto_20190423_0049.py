# Generated by Django 2.2 on 2019-04-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmovements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhead',
            name='amount',
            field=models.IntegerField(db_column='Traded Amount'),
        ),
        migrations.AlterField(
            model_name='stockhead',
            name='index',
            field=models.IntegerField(db_column='S.No'),
        ),
        migrations.AlterField(
            model_name='stockhead',
            name='tradedshares',
            field=models.IntegerField(db_column='Traded Shares'),
        ),
        migrations.AlterField(
            model_name='stockhead',
            name='transactions',
            field=models.IntegerField(db_column='No of Transactions'),
        ),
    ]
