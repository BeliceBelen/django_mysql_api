# Generated by Django 4.0.5 on 2022-06-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_fichainscripcion_ciudad_fichainscripcion_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichainscripcion',
            name='fechaInscripcion',
            field=models.DateField(),
        ),
    ]