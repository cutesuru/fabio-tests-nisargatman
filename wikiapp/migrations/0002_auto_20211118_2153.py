# Generated by Django 3.2.6 on 2021-11-18 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wikiapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='id',
            new_name='uuid',
        ),
        migrations.RenameField(
            model_name='continent',
            old_name='id',
            new_name='uuid',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='id',
            new_name='uuid',
        ),
    ]