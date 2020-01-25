# Generated by Django 2.2.6 on 2020-01-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20191221_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalCurrent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('weather_id', models.IntegerField()),
                ('weather_main', models.TextField()),
                ('weather_description', models.TextField()),
                ('weather_icon', models.TextField()),
                ('temperature', models.TextField()),
                ('feels_like', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('pressure', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_speed', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_direction', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('cloud', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('rain_one_hour', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('rain_three_hour', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('snow_one_hour', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('snow_three_hour', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('calculation_datatime', models.DateField()),
                ('city_country', models.TextField()),
                ('city_id', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('city_name', models.TextField()),
                ('update_time', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalPredict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_country', models.TextField()),
                ('city_name', models.TextField()),
                ('city_id', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('update_time', models.TimeField(auto_now=True)),
                ('weather_id_one', models.IntegerField()),
                ('weather_main_one', models.TextField()),
                ('weather_description_one', models.TextField()),
                ('weather_icon_one', models.TextField()),
                ('temperatur_one', models.TextField()),
                ('feels_like_one', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('pressure_one', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('humidity_one', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_speed_one', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_direction_one', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('cloud_one', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('predict_time_one', models.DateTimeField()),
                ('weather_id_two', models.IntegerField()),
                ('weather_main_two', models.TextField()),
                ('weather_description_two', models.TextField()),
                ('weather_icon_two', models.TextField()),
                ('temperatur_two', models.TextField()),
                ('feels_like_two', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('pressure_two', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('humidity_two', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_speed_two', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_direction_two', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('cloud_two', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('predict_time_two', models.DateTimeField()),
                ('weather_id_three', models.IntegerField()),
                ('weather_main_three', models.TextField()),
                ('weather_description_three', models.TextField()),
                ('weather_icon_three', models.TextField()),
                ('temperatur_three', models.TextField()),
                ('feels_like_three', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('pressure_three', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('humidity_three', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_speed_three', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_direction_three', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('cloud_three', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('predict_time_three', models.DateTimeField()),
                ('weather_id_four', models.IntegerField()),
                ('weather_main_four', models.TextField()),
                ('weather_description_four', models.TextField()),
                ('weather_icon_four', models.TextField()),
                ('temperatur_four', models.TextField()),
                ('feels_like_four', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('pressure_four', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('humidity_four', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_speed_four', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_direction_four', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('cloud_four', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('predict_time_four', models.DateTimeField()),
                ('weather_id_five', models.IntegerField()),
                ('weather_main_five', models.TextField()),
                ('weather_description_five', models.TextField()),
                ('weather_icon_five', models.TextField()),
                ('temperatur_five', models.TextField()),
                ('feels_like_five', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('pressure_five', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('humidity_five', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_speed_five', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_direction_five', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('cloud_five', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('predict_time_five', models.DateTimeField()),
                ('weather_id_six', models.IntegerField()),
                ('weather_main_six', models.TextField()),
                ('weather_description_six', models.TextField()),
                ('weather_icon_six', models.TextField()),
                ('temperatur_six', models.TextField()),
                ('feels_like_six', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('pressure_six', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('humidity_six', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_speed_six', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_direction_six', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('cloud_six', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('predict_time_six', models.DateTimeField()),
                ('weather_id_seven', models.IntegerField()),
                ('weather_main_seven', models.TextField()),
                ('weather_description_seven', models.TextField()),
                ('weather_icon_seven', models.TextField()),
                ('temperatur_seven', models.TextField()),
                ('feels_like_seven', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('pressure_seven', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('humidity_seven', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_speed_seven', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_direction_seven', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('cloud_seven', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('predict_time_seven', models.DateTimeField()),
                ('weather_id_eight', models.IntegerField()),
                ('weather_main_eight', models.TextField()),
                ('weather_description_eight', models.TextField()),
                ('weather_icon_eight', models.TextField()),
                ('temperatur_eight', models.TextField()),
                ('feels_like_eight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('pressure_eight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('humidity_eight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_speed_eight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('wind_direction_eight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('cloud_eight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('predict_time_eight', models.DateTimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='CurrentWeather',
            new_name='DomesticCurrent',
        ),
        migrations.DeleteModel(
            name='ShortPredictionWeather',
        ),
    ]