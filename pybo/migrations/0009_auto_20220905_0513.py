# Generated by Django 3.1.3 on 2022-09-04 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0008_similar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='similar',
            name='similar',
            field=models.IntegerField(default=0),
        ),
    ]
