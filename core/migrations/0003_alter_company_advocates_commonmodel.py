# Generated by Django 4.1.2 on 2022-10-14 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_company_href'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='advocates',
            field=models.ManyToManyField(blank=True, default='', related_name='advocates', to='core.advocate'),
        ),
        migrations.CreateModel(
            name='Commonmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advocate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.advocate')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.company')),
            ],
        ),
    ]
