# Generated by Django 2.2.5 on 2019-11-03 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca', '0008_auto_20191029_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='libro',
            name='copias',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
