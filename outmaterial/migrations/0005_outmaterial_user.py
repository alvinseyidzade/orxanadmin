# Generated by Django 2.2 on 2019-04-17 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('outmaterial', '0004_auto_20190417_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='outmaterial',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outmaterial', to=settings.AUTH_USER_MODEL),
        ),
    ]
