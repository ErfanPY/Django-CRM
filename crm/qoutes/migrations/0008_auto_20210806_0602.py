# Generated by Django 3.2.5 on 2021-08-06 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qoutes', '0007_emails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emails',
            options={'ordering': ('send_date',), 'verbose_name': 'ایمیل', 'verbose_name_plural': 'ایمیل ها'},
        ),
        migrations.RenameField(
            model_name='emails',
            old_name='send_data',
            new_name='send_date',
        ),
    ]
