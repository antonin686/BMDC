# Generated by Django 3.0.2 on 2020-02-03 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='registration_no',
            field=models.IntegerField(),
        ),
    ]
