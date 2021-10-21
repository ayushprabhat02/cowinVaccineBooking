# Generated by Django 3.2.8 on 2021-10-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ayushVaccineSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('pincode', models.IntegerField(default='null')),
                ('date', models.CharField(max_length=200)),
                ('vaccine_type', models.CharField(blank=True, default='null', max_length=200, null=True)),
                ('min_age_limit', models.IntegerField(blank=True, default='null', null=True)),
                ('available_capacity', models.IntegerField(blank=True, default='null', null=True)),
            ],
            options={
                'db_table': 'ayushVaccineSlot',
            },
        ),
        migrations.AlterField(
            model_name='member_info_class',
            name='first_booking',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member_info_class',
            name='second_booking',
            field=models.DateField(blank=True, null=True),
        ),
    ]
