# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(unique=True, max_length=128, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('info', models.CharField(max_length=50, verbose_name='\u7b80\u77ed\u4f18\u52bf')),
                ('image', models.ImageField(upload_to=b'market/category/', verbose_name='\u5206\u7c7b\u56fe\u7247', blank=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('code', models.CharField(max_length=50, null=True, verbose_name='\u5206\u7c7b\u7f16\u53f7', blank=True)),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0', blank=True)),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u540e\u53f0\u6743\u9650',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('mobile', models.CharField(max_length=20, verbose_name='\u624b\u673a\u53f7', blank=True)),
                ('tel', models.CharField(max_length=20, verbose_name='\u8054\u7cfb\u65b9\u5f0f', blank=True)),
                ('image', models.ImageField(upload_to=b'market/category/', verbose_name='\u5206\u7c7b\u56fe\u7247', blank=True)),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0', blank=True)),
                ('manager', models.CharField(max_length=20, verbose_name='\u8d1f\u8d23\u4eba')),
            ],
            options={
                'verbose_name': '\u516c\u53f8',
                'verbose_name_plural': '\u516c\u53f8',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(unique=True, max_length=128, verbose_name='\u540d\u79f0')),
                ('code', models.CharField(max_length=50, null=True, verbose_name='\u5546\u54c1\u7f16\u7801', blank=True)),
                ('info', models.CharField(max_length=50, verbose_name='\u7b80\u77ed\u4f18\u52bf')),
                ('image', models.ImageField(upload_to=b'market/product/', verbose_name='\u5546\u54c1\u56fe\u7247\u56fe\u7247', blank=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0', blank=True)),
                ('materials', models.TextField(verbose_name='\u914d\u6599', blank=True)),
                ('category', models.ForeignKey(verbose_name='\u6240\u5c5e\u5206\u7c7b', to='market.Category')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u8868',
                'verbose_name_plural': '\u5546\u54c1\u8868',
            },
        ),
    ]
