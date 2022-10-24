# Generated by Django 4.1 on 2022-10-24 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_apipreferencemodel_pays_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apipreferencemodel',
            name='pays_de_depart',
            field=models.CharField(choices=[('FR', 'France'), ('AR', 'Argentine'), ('UK', 'Royaume-Uni'), ('IT', 'Italie'), ('USA', 'Etats-Unis')], default='FR', max_length=3),
        ),
    ]