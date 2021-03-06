# Generated by Django 3.0.2 on 2020-02-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starwarsapi', '0008_auto_20200203_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='movies',
            field=models.ManyToManyField(through='starwarsapi.CharacterMovie', to='starwarsapi.Movie'),
        ),
        migrations.AddField(
            model_name='character',
            name='role',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='force_sensitive',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
