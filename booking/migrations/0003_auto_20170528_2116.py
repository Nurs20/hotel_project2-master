# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20170528_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('1', 'Заявка подана'), ('2', 'Рассмотрена'), ('3', 'Подтверждена'), ('4', 'Отклонена')], max_length=15, null=True, verbose_name='Статус'),
        ),
    ]