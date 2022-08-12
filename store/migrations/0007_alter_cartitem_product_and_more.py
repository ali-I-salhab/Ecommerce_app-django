# Generated by Django 4.0.6 on 2022-08-11 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_cart_id_alter_collection_featured_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.product'),
        ),
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={()},
        ),
    ]