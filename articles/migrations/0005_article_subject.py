# Generated by Django 3.1.7 on 2021-04-05 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210405_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='articles.subject'),
            preserve_default=False,
        ),
    ]
