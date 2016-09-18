# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dhcp_file_path', models.CharField(max_length=100)),
                ('network', models.GenericIPAddressField(protocol='IPv4')),
                ('netmask', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
