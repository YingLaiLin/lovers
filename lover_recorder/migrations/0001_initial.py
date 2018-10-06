# Generated by Django 2.1.2 on 2018-10-06 05:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('abstract', models.TextField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='发生时间')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20, verbose_name='登录名')),
                ('icon', models.ImageField(default=None, height_field=200, upload_to='', verbose_name='头像', width_field=200)),
                ('nickname', models.CharField(max_length=40, verbose_name='昵称')),
                ('authority', models.IntegerField(default=0, verbose_name='在网站中的权限')),
                ('level', models.IntegerField(default=0, verbose_name='用户等级')),
                ('type', models.IntegerField(choices=[(0, '游客'), (1, '用户'), (2, '管理员'), (3, '网站所有者')], default=0, verbose_name='用户类别')),
                ('register_date', models.DateTimeField(verbose_name='注册时间')),
                ('login_time', models.DateTimeField(verbose_name='上次登录时间')),
            ],
        ),
    ]
