# Generated by Django 5.0.7 on 2024-09-25 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_description_experience_responsibilities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='project_links',
            new_name='project_link',
        ),
    ]
