# Generated by Django 4.1.7 on 2023-03-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerUserApp', '0007_alter_customeruser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
