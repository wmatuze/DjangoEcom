# Generated by Django 3.0.5 on 2020-05-08 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShippingAddress',
            new_name='DeliveryAddress',
        ),
        migrations.RenameField(
            model_name='deliveryaddress',
            old_name='house_no',
            new_name='houseno',
        ),
    ]
