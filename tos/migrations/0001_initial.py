# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TermsOfService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(help_text='Only one terms of service is allowed to be active', verbose_name='active')),
                ('content', models.TextField(verbose_name='content', blank=True)),
            ],
            options={
                'ordering': ('-created',),
                'get_latest_by': 'created',
                'verbose_name': 'Terms of Service',
                'verbose_name_plural': 'Terms of Service',
            },
        ),
        migrations.CreateModel(
            name='UserAgreement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('terms_of_service', models.ForeignKey(related_name='terms', to='tos.TermsOfService')),
                ('user', models.ForeignKey(related_name='user_agreement', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
