# Generated by Django 4.0.1 on 2024-07-20 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_user_last_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='cat_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
    ]
