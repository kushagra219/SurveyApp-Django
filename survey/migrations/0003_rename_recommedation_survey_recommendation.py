# Generated by Django 3.2.3 on 2021-06-25 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20210620_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='recommedation',
            new_name='recommendation',
        ),
    ]
