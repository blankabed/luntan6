# Generated by Django 3.0.2 on 2020-02-17 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bisheapp', '0002_auto_20200205_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_uid', models.CharField(max_length=16, verbose_name='帖子所属用户id')),
                ('t_kind', models.CharField(max_length=32, verbose_name='类别')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('t_photo', models.CharField(max_length=128, null=True, verbose_name='帖子图片')),
                ('t_content', models.CharField(max_length=3000, verbose_name='帖子正文')),
                ('t_title', models.CharField(max_length=64, verbose_name='帖子标题')),
                ('t_introduce', models.CharField(max_length=256, verbose_name='帖子简介')),
                ('recommend', models.BooleanField(default=False, verbose_name='是否推荐')),
            ],
        ),
    ]