# Generated by Django 2.1.5 on 2019-01-25 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0004_auto_20190125_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='operators',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opera', to='mobile.Operators'),
        ),
    ]