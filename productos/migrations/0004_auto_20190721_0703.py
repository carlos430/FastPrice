# Generated by Django 2.2.3 on 2019-07-21 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20190721_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
