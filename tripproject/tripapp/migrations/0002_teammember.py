# Generated by Django 5.0.1 on 2024-04-18 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
    ]
