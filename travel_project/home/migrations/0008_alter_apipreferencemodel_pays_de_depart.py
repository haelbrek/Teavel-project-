# Generated by Django 4.1 on 2022-11-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_apipreferencemodel_pays_de_depart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apipreferencemodel',
            name='pays_de_depart',
            field=models.CharField(choices=[('FR', 'France'), ('AR', 'Argentine'), ('GB', 'Royaume-Uni'), ('IT', 'Italie'), ('US', 'Etats-Unis'), ('DE', 'Allemagne'), ('ES', 'Espagne'), ('NL', 'Pays-bas'), ('MX', 'Mexique'), ('SA', 'Arabie saoudite')], max_length=3, null=True),
        ),
    ]
