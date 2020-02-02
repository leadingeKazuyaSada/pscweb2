# Generated by Django 3.0.2 on 2020-01-28 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_auto_20190818_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_dt', models.DateTimeField(verbose_name='期限')),
                ('invitee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitee', to='production.ProdUser', verbose_name='招待された人')),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inviter', to='production.ProdUser', verbose_name='招待主')),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.Production', verbose_name='公演')),
            ],
            options={
                'verbose_name': '座組への招待',
                'verbose_name_plural': '座組への招待',
            },
        ),
    ]
