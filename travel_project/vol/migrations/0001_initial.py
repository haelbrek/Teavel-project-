# Generated by Django 4.1 on 2022-10-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vols',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('date_depart', models.CharField(max_length=100)),
                ('date_arrive', models.CharField(max_length=100)),
                ('classe_vol', models.CharField(max_length=3)),
            ],
        ),
    ]
