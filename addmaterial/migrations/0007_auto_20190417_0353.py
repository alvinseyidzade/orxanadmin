# Generated by Django 2.2 on 2019-04-17 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addmaterial', '0006_addmaterial_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addmaterial',
            old_name='product_type',
            new_name='product_typeadd',
        ),
    ]