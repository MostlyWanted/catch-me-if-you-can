# Generated by Django 3.2.6 on 2021-08-31 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='locations',
            field=models.ManyToManyField(to='main_app.Location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='location_name',
            field=models.CharField(choices=[('CANADA', 'CANADA'), ('USA', 'USA'), ('ARCTIC', 'ARCTIC')], max_length=200),
        ),
    ]
