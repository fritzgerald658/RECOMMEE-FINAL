# Generated by Django 5.0.2 on 2024-04-29 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesisapp', '0016_delete_userhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictionresult',
            name='user_history_id',
            field=models.IntegerField(null=True),
        ),
    ]