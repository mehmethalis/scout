# Generated by Django 4.1.1 on 2022-09-26 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_candidate_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='bio',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
