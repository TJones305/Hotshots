# Generated by Django 3.2.8 on 2021-11-26 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0003_product_has_sizes'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreview',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_review', to='products.product'),
        ),
        migrations.AlterField(
            model_name='userreview',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review_creator', to='profiles.userprofile'),
        ),
    ]
