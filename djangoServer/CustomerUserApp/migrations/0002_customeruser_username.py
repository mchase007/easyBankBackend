# Generated by Django 4.1.7 on 2023-03-02 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerUserApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='username',
            field=models.CharField(default='default_username', max_length=50, unique=True),
        ),
    ]
