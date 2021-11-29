# Generated by Django 3.2.8 on 2021-11-29 13:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20211128_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreview',
            name='review_rating',
            field=models.IntegerField(blank=True, choices=[(0, 'No Rating -- 0'), (1, 'Stay Away -- 1'), (2, 'Subpar -- 2'), (3, 'OK -- 3'), (4, 'Great -- 4'), (5, 'Excellent -- 5')], default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
