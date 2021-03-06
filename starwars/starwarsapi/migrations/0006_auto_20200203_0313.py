# Generated by Django 3.0.2 on 2020-02-03 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starwarsapi', '0005_auto_20200203_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='gender',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='planet',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='species',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='climate',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='terrain',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='species',
            name='classification',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='species',
            name='language',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='manufacturer',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='max_speed',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='passengers',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='starship',
            name='starship_class',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='manufacturer',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='max_speed',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='passengers',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_class',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
