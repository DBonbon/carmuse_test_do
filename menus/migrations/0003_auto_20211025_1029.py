# Generated by Django 3.0.2 on 2021-10-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_auto_20211019_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
