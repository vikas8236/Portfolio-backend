# Generated by Django 5.0.7 on 2024-09-25 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_rename_proficiency_level_skill_proficiency_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.CharField(choices=[('technical', 'Technical Skill'), ('professional', 'Professional Skills'), ('social', 'Social Skills'), ('other', 'Other Skill')], default='technical', max_length=50),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_type',
            field=models.CharField(choices=[('frontend', 'Frontend Development'), ('backend', 'Backend Development'), ('database', 'Database Management'), ('management', 'Project Management'), ('other', 'Other Skills')], default='frontend', max_length=50),
        ),
    ]
