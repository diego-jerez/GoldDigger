# Generated by Django 3.1.4 on 2021-01-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GDapp', '0012_emimage_output_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emimage',
            name='threshold_string',
            field=models.CharField(blank=True, default='1, 300', max_length=200),
        ),
    ]
