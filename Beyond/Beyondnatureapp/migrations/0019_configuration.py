# Generated by Django 4.1 on 2023-06-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beyondnatureapp', '0018_amenities_delete_amenities_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_bedrooms', models.TextField(max_length=30)),
                ('sq_ft', models.TextField(max_length=30)),
            ],
        ),
    ]
