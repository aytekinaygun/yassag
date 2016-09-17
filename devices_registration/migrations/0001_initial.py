# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices_Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_status', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.CharField(max_length=60)),
                ('note', models.CharField(max_length=300, null=True, blank=True)),
                ('device_status', models.IntegerField(default=0)),
                ('transaction_date', models.DateTimeField(null=True, blank=True)),
                ('ip', models.GenericIPAddressField(protocol='IPv4')),
                ('mac', models.CharField(max_length=20)),
                ('device', models.ForeignKey(to='devices_registration.Devices_Status')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users_Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_status', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='users',
            name='status',
            field=models.ForeignKey(to='devices_registration.Users_Status'),
            preserve_default=True,
        ),
    ]
