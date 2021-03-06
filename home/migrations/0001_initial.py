# Generated by Django 3.2 on 2021-05-09 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(max_length=800)),
            ],
            options={
                'verbose_name_plural': 'About Section',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(choices=[('instagram', 'Instagram'), ('facebook', 'Facebook'), ('tiktok', 'Tiktok'), ('pinterest', 'Pintereset'), ('youtube', 'Youtube'), ('snapchat', 'Snapchat'), ('twitter', 'Twitter')], max_length=254)),
                ('icon', models.CharField(choices=[('fa-instagram', 'Instagram'), ('fa-facebook-f', 'Facebook'), ('fa-tiktok', 'Tiktok'), ('fa-pinterest-p', 'Pintereset'), ('fa-youtube', 'Youtube'), ('fa-snapchat-ghost', 'Snapchat'), ('fa-twitter', 'Twitter')], max_length=50)),
                ('url', models.URLField(blank=True, default='', max_length=1024, null=True)),
            ],
            options={
                'verbose_name_plural': 'Social Media Icons',
            },
        ),
    ]
