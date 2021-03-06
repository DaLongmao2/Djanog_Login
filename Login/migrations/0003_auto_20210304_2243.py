# Generated by Django 3.1.7 on 2021-03-04 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_auto_20210304_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isdelete',
            field=models.BooleanField(default=False, verbose_name='逻辑删除'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='未设置', max_length=30, verbose_name='用户名'),
        ),
    ]