# Generated by Django 3.0.8 on 2020-07-06 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='approved',
            new_name='deleted',
        ),
    ]
