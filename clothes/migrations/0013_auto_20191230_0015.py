# Generated by Django 2.2.6 on 2019-12-29 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0012_auto_20191229_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothing',
            name='img',
            field=models.ImageField(default='deepfashion12291159default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
