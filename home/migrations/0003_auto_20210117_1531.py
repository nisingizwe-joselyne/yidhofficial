# Generated by Django 3.1.5 on 2021-01-17 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210117_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.farmers'),
        ),
    ]
