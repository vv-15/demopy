# Generated by Django 4.2 on 2023-06-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
