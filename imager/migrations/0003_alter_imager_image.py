# Generated by Django 3.2.9 on 2022-04-06 16:43

from django.db import migrations, models
import imager.models


class Migration(migrations.Migration):

    dependencies = [
        ('imager', '0002_alter_imager_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imager',
            name='image',
            field=models.ImageField(upload_to=imager.models.userPath),
        ),
    ]