# Generated by Django 3.1.7 on 2021-03-04 17:24

import Login.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=18, verbose_name='年龄'),
        ),
        migrations.AddField(
            model_name='user',
            name='bgcolor',
            field=models.CharField(default='#6f9388', max_length=50, verbose_name='背景颜色'),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=100, unique=True, verbose_name='邮箱'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.BooleanField(default=True, verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='+86 999-999-999', max_length=100, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=models.UUIDField(default=Login.models.UUIDTools.uuid1_hex, editable=False, primary_key=True, serialize=False), max_length=30, verbose_name='用户名'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
        migrations.DeleteModel(
            name='LoginTime',
        ),
    ]
