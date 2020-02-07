# Generated by Django 3.0.2 on 2020-02-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starwarsapi', '0015_planet_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(max_length=200, null=True)),
                ('planet', models.CharField(max_length=200, null=True)),
                ('species', models.CharField(max_length=200, null=True)),
                ('image', models.CharField(max_length=200, null=True)),
                ('force_sensitive', models.BooleanField(blank=True, null=True)),
                ('side', models.CharField(blank=True, max_length=200, null=True)),
                ('role', models.CharField(blank=True, max_length=200, null=True)),
                ('best_quote', models.CharField(blank=True, max_length=200, null=True)),
                ('lightsaber', models.CharField(blank=True, max_length=200, null=True)),
                ('sith_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserPlanet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('climate', models.CharField(max_length=200, null=True)),
                ('terrain', models.CharField(max_length=200, null=True)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wildlife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('classification', models.CharField(blank=True, max_length=200, null=True)),
                ('habitat', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
