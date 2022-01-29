# Generated by Django 3.2.5 on 2021-08-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qoutes', '0004_alter_qoute_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qouteproductdetail',
            name='discount_percent',
            field=models.PositiveIntegerField(verbose_name='درصد تخفیف'),
        ),
        migrations.AlterField(
            model_name='qouteproductdetail',
            name='price',
            field=models.PositiveIntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='qouteproductdetail',
            name='qty',
            field=models.PositiveIntegerField(verbose_name='تعداد'),
        ),
    ]
