# Generated by Django 4.1 on 2022-08-18 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_note_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='complete',
        ),
    ]