# Generated by Django 3.2.7 on 2021-09-08 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
