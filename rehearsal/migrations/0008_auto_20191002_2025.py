# Generated by Django 2.2.5 on 2019-10-02 11:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rehearsal', '0007_scncomment_mod_prod_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appearance',
            name='lines_num',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='セリフ数'),
        ),
        migrations.AlterField(
            model_name='scncomment',
            name='mod_prod_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='production.ProdUser', verbose_name='記入者'),
        ),
    ]
