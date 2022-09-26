# Generated by Django 4.1.1 on 2022-09-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='avatar_url',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='company',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.EmailField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hireable',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='website',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]