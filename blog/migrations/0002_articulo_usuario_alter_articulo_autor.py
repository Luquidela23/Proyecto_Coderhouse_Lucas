# Generated by Django 4.2.7 on 2023-11-24 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='articulos_usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articulos_autor', to=settings.AUTH_USER_MODEL),
        ),
    ]
