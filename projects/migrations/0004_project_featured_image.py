# Generated by Django 4.1.7 on 2023-03-09 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_rename_reviw_review_project_vote_ratio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
