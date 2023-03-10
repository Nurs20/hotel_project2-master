# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 11:12
from __future__ import unicode_literals

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
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_date', models.DateField(verbose_name='День заезда')),
                ('e_date', models.DateField(verbose_name='День выезда')),
                ('room', models.SmallIntegerField(null=True, verbose_name='Комната')),
                ('style', models.CharField(choices=[('budget', 'Бюджетный'), ('business', 'Бизнесс-класс'), ('lux', 'Люкс')], max_length=15, verbose_name='Класс аппартаментов')),
                ('status', models.SmallIntegerField(choices=[('budget', 'Бюджетный'), ('business', 'Бизнесс-класс'), ('lux', 'Люкс')], null=True, verbose_name='Статус')),
                ('comment', models.CharField(max_length=500, verbose_name='Коментарий')),
                ('child', models.SmallIntegerField(verbose_name='Количество детей')),
                ('number_peoples', models.SmallIntegerField(verbose_name='Количество людей')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Время бронирования')),
                ('price', models.IntegerField(null=True, verbose_name='Цена')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Бронь',
                'verbose_name_plural': 'Брони',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('housing', models.SmallIntegerField(verbose_name='Корпус')),
                ('floor', models.SmallIntegerField(verbose_name='Этаж')),
                ('number', models.SmallIntegerField(verbose_name='Номер')),
                ('per_night', models.SmallIntegerField(verbose_name='Стоимость за ночь')),
                ('number_beds', models.SmallIntegerField(verbose_name='Количество спальных мест')),
                ('style', models.CharField(choices=[('budget', 'Бюджетный'), ('business', 'Бизнесс-класс'), ('lux', 'Люкс')], max_length=15, verbose_name='Класс аппартаментов')),
            ],
        ),
    ]
