# Generated by Django 3.1.7 on 2021-04-05 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210405_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='title',
        ),
    ]