# Generated by Django 4.2 on 2024-06-09 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('note_type', models.IntegerField(choices=[(0, 'default'), (1, 'image'), (2, 'checkbox')], default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('checkbox_list', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
