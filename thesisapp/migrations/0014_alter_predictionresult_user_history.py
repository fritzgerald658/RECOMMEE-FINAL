# Generated by Django 5.0.2 on 2024-04-26 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesisapp', '0013_alter_predictionresult_user_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictionresult',
            name='user_history',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='thesisapp.userhistory'),
        ),
    ]
