# Generated by Django 3.2 on 2022-01-22 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Content',
            new_name='content',
        ),
    ]
