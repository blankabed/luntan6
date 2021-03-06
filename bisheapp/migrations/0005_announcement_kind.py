# Generated by Django 2.0.6 on 2020-02-26 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bisheapp', '0004_auto_20200221_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_title', models.CharField(max_length=64, verbose_name='公告标题')),
                ('a_content', models.CharField(max_length=3000, null=True, verbose_name='公告内容')),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('k_name', models.CharField(max_length=16, verbose_name='分类名称')),
            ],
        ),
    ]
