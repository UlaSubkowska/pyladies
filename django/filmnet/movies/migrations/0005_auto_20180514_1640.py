# Generated by Django 2.0.5 on 2018-05-14 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20180514_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('horror', 'Horror'), ('horror_for_kids', 'Horror 4 kids'), ('fantasy', 'Fantasy'), ('drama', 'Drama'), ('comedy', 'Comedy')], max_length=50),
        ),
    ]
