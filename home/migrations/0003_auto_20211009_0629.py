# Generated by Django 3.2.8 on 2021-10-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211009_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccineslot',
            name='pin_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vaccineslot',
            name='vaccine_12',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vaccineslot',
            name='vaccine_18',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vaccineslot',
            name='vaccine_45',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vaccineslot',
            name='vaccine_60',
            field=models.IntegerField(),
        ),
    ]