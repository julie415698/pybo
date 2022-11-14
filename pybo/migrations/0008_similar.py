# Generated by Django 3.1.3 on 2022-09-04 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0007_remove_maincont_similar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Similar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similar', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('maincont', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pybo.maincont')),
            ],
        ),
    ]
