# Generated by Django 2.2.6 on 2019-11-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_auto_20191007_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='img_perfil',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
