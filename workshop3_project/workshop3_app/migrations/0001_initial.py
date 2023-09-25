# Generated by Django 4.2.5 on 2023-09-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ATTN_Number', models.IntegerField()),
                ('Movie_Name', models.TextField()),
                ('Seat_Number', models.TextField()),
                ('Show_Time', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('year', models.TextField()),
                ('genre', models.TextField()),
            ],
        ),
    ]
