# Generated by Django 5.0.7 on 2024-09-24 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_projects_skills'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='related_projects',
            new_name='projects',
        ),
    ]
