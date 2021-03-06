# Generated by Django 2.2.3 on 2019-09-08 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShipDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imo', models.BigIntegerField()),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'ship_detail',
            },
        ),
        migrations.CreateModel(
            name='ShipPositionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imo', models.BigIntegerField()),
                ('position_dt_tm', models.DateTimeField()),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=11)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 9, 8, 12, 34, 8, 477467))),
            ],
            options={
                'db_table': 'ship_position_details',
            },
        ),
        migrations.AddConstraint(
            model_name='shippositiondetails',
            constraint=models.UniqueConstraint(fields=('imo', 'position_dt_tm'), name='imo_position_dt_uniq'),
        ),
        migrations.AddConstraint(
            model_name='shipdetail',
            constraint=models.UniqueConstraint(fields=('imo', 'name'), name='ship_name_uniq'),
        ),
    ]
