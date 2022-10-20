# Generated by Django 4.1.2 on 2022-10-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_company_advocates_commonmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocate',
            name='profile_pic',
            field=models.URLField(max_length=300),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.URLField(max_length=300),
        ),
        migrations.DeleteModel(
            name='Commonmodel',
        ),
    ]
