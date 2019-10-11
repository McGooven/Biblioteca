# Generated by Django 2.2.5 on 2019-10-03 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Biblioteca', '0002_auto_20190922_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstanciaLibro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fech_inicio', models.DateField(verbose_name='Fecha de entrega')),
                ('fech_vencimiento', models.DateField(verbose_name='Fecha de devolución')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Biblioteca.Libro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]