# Generated by Django 4.1 on 2022-10-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_apipreferencemodel_pays_de_depart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apipreferencemodel',
            name='pays_de_depart',
            field=models.CharField(choices=[('FR', 'France'), ('AR', 'Argentine'), ('GB', 'Royaume-Uni'), ('IT', 'Italie'), ('US', 'Etats-Unis')], max_length=3),
        ),
    ]