# Generated by Django 4.1.1 on 2022-09-26 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_candidate_avatar_url_alter_candidate_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='bio',
            field=models.CharField(max_length=250),
        ),
    ]
