# Generated by Django 5.1.4 on 2025-01-20 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='product',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='seller',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
