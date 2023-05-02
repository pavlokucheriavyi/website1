# Generated by Django 3.2.6 on 2021-09-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210910_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='shop_sizes',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X Large')], default='S', max_length=2),
        ),
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=1, verbose_name='Просmотры'),
        ),
    ]
