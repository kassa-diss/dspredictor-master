# Generated by Django 3.1.7 on 2021-04-17 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_myworks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myworks',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.patient'),
        ),
    ]
