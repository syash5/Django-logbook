# Generated by Django 3.0.8 on 2021-04-28 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logentries', '0002_auto_20210429_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='getuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
