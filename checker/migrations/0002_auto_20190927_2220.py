# Generated by Django 2.2.5 on 2019-09-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checker',
            name='code',
            field=models.FileField(upload_to='uploads/checkers'),
        ),
    ]