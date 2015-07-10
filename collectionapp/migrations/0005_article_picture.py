# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collectionapp', '0004_auto_20150710_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(default='photos/None/no-img.jpg', upload_to='photos/'),
            preserve_default=True,
        ),
    ]
