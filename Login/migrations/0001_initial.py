# Generated by Django 3.1.7 on 2021-03-03 01:46

import Login.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=Login.models.UUIDTools.uuid1_hex, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='LoginTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_record', models.DateTimeField(auto_now_add=True)),
                ('login_UserAgent', models.CharField(max_length=256)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.user')),
            ],
        ),
    ]
