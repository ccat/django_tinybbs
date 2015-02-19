# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('nickname', models.CharField(max_length=512)),
                ('content', models.TextField(default=b'')),
                ('deletekey', models.CharField(max_length=512, null=True, blank=True)),
                ('is_disabled', models.BooleanField(default=False)),
                ('read_auth', models.CharField(default=b'e', max_length=3, choices=[(b'e', b'everyone'), (b's', b'staff'), (b'u', b'users')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(unique=True, max_length=2048)),
                ('title', models.CharField(max_length=1024)),
                ('read_auth', models.CharField(default=b'e', max_length=3, choices=[(b'e', b'everyone'), (b's', b'staff'), (b'u', b'users')])),
                ('write_auth', models.CharField(default=b'e', max_length=3, choices=[(b'e', b'everyone'), (b's', b'staff'), (b'u', b'users')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(to='tinybbs.Topic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
