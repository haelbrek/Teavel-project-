# Generated by Django 4.1 on 2022-11-03 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_alter_hotels_nombre_etoiles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='nombre_etoiles',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='services_equipements',
            field=models.CharField(choices=[('SWIMMING_POOL', 'Piscine'), ('SPA', 'SPA'), ('RESTAURANT', 'Restaurant'), ('PETS_ALLOWED', 'Animaux autorisés'), ('BEACH', 'Plage'), ('FITNESS_CENTER', 'Salle de sport'), ('AIRPORT_SHUTTLE', 'navette aéroport'), (' MASSAGE', 'Massage'), ('BAR or LOUNGE', 'Bar'), ('ROOM_SERVICE', 'Room Service')], default='SPA', max_length=150, null=True),
        ),
    ]
