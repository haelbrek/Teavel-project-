# Generated by Django 4.1 on 2022-10-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apipreferencemodel',
            name='pays',
        ),
        migrations.AddField(
            model_name='apipreferencemodel',
            name='pays_de_depart',
            field=models.CharField(choices=[('FR', 'france'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
    ]
