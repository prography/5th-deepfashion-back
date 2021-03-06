# Generated by Django 2.2.6 on 2019-12-19 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clothes', '0005_auto_20191218_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodiList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('clothes', models.ManyToManyField(to='clothes.Clothing')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codis', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
