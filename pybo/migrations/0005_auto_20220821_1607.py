# Generated by Django 3.1.3 on 2022-08-21 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='maincont',
            name='voter',
            field=models.ManyToManyField(related_name='voter_maincont', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='maincont',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_maincont', to=settings.AUTH_USER_MODEL),
        ),
    ]
