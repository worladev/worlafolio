# Generated by Django 5.1.2 on 2024-10-14 17:25

import folio.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='technologies',
            field=folio.fields.CustomTagsField(max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='skills',
            field=folio.fields.CustomTagsField(blank=True, max_length=250),
        ),
    ]
