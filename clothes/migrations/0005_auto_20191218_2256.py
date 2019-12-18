# Generated by Django 2.2.6 on 2019-12-18 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0004_auto_20191117_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='clothing',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clothes.ColorType'),
        ),
    ]
