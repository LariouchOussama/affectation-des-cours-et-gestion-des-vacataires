# Generated by Django 4.2.2 on 2023-06-11 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_absence_operationhistory_vacataire_contrat'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacataire',
            name='dept',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='vacataire',
            name='present',
            field=models.BooleanField(default=False),
        ),
    ]
