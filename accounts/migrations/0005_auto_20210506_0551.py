# Generated by Django 3.1 on 2021-05-06 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_invoice_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='childID',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='surname',
        ),
    ]
