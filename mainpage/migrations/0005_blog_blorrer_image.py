# Generated by Django 4.2.5 on 2024-04-09 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blorrer_image',
            field=models.ImageField(default=0, upload_to='productimages'),
        ),
    ]
