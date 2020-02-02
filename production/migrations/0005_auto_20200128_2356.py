# Generated by Django 3.0.2 on 2020-01-28 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('production', '0004_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='invitee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitee', to=settings.AUTH_USER_MODEL, verbose_name='招待される人'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='inviter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inviter', to=settings.AUTH_USER_MODEL, verbose_name='招待する人'),
        ),
    ]
