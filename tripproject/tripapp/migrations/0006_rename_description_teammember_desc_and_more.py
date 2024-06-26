# Generated by Django 5.0.1 on 2024-04-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripapp', '0005_alter_teammember_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammember',
            old_name='description',
            new_name='desc',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='image',
        ),
        migrations.AddField(
            model_name='teammember',
            name='img',
            field=models.ImageField(default='jkbb', upload_to='team_images/'),
            preserve_default=False,
        ),
    ]
