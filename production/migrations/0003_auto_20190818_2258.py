# Generated by Django 2.2.4 on 2019-08-18 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_auto_20190817_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produser',
            old_name='prod_id',
            new_name='production',
        ),
        migrations.RenameField(
            model_name='produser',
            old_name='user_id',
            new_name='user',
        ),
    ]