# Generated by Django 3.0.1 on 2020-01-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racetime', '0007_auto_20200118_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_bio',
            field=models.TextField(blank=True, help_text='Add some information to your public profile. Plug your Discord server, stream schedule, or anything else you like.', null=True),
        ),
    ]
