# Generated by Django 4.0.5 on 2022-06-10 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('num_seats', models.IntegerField()),
                ('wheel_size', models.CharField(max_length=50)),
                ('car_type', models.CharField(choices=[('suv', 'SUV'), ('sports car', 'Sports Car'), ('van', 'Van'), ('pickup', 'PickUp')], default='SUV', max_length=10)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-price',),
            },
        ),
    ]
