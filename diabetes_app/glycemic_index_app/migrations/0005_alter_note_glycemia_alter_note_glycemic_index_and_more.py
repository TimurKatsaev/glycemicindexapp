# Generated by Django 4.2.14 on 2024-08-31 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glycemic_index_app', '0004_alter_note_glycemia_alter_note_glycemic_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='glycemia',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='note',
            name='glycemic_index',
            field=models.CharField(max_length=500),
        ),
        migrations.DeleteModel(
            name='Statistics',
        ),
    ]
