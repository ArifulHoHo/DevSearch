# Generated by Django 4.1.7 on 2023-03-24 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_options_review_owner_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
