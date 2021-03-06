# Generated by Django 2.2.8 on 2019-12-29 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='題名')),
                ('author', models.CharField(blank=True, max_length=50, verbose_name='著者')),
                ('raw_data', models.TextField(blank=True, verbose_name='データ')),
                ('format', models.IntegerField(choices=[(1, 'Fountain JA')], default=1, verbose_name='フォーマット')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='変更日時')),
                ('public_level', models.IntegerField(choices=[(1, '公開しない'), (2, 'PSCWEB2 ユーザ')], default=1, verbose_name='公開レベル')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所有者')),
            ],
            options={
                'verbose_name': '台本',
                'verbose_name_plural': '台本',
            },
        ),
    ]
