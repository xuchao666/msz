# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_company_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=64, verbose_name='\u540d\u79f0')),
                ('image', models.ImageField(upload_to=b'market/', verbose_name='\u9996\u9875\u8f6e\u64ad\u56fe\u7247', blank=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='\u662f\u5426\u662f\u9996\u5f20\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u9996\u9875\u8f6e\u64ad\u56fe',
                'verbose_name_plural': '\u9996\u9875\u8f6e\u64ad\u56fe',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u5206\u7c7b', 'verbose_name_plural': '\u5206\u7c7b'},
        ),
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(upload_to=b'market/category/', verbose_name='\u516c\u53f8\u56fe\u7247', blank=True),
        ),
    ]
