# Generated by Django 4.1.7 on 2023-03-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerUserApp', '0004_remove_customeruser_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
