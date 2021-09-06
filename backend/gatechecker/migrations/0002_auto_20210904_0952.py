# Generated by Django 2.2 on 2021-09-04 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gatechecker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='to_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gatechecker.User'),
        ),
        migrations.AlterField(
            model_name='device',
            name='to_gate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gatechecker.Gate'),
        ),
        migrations.AlterField(
            model_name='gate',
            name='to_building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gatechecker.Building'),
        ),
        migrations.AlterField(
            model_name='log',
            name='to_device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gatechecker.Device'),
        ),
    ]
