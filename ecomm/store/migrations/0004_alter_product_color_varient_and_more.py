# Generated by Django 5.0.3 on 2024-03-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_colorvarient_sizevarient_alter_productimage_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color_varient',
            field=models.ManyToManyField(blank=True, to='store.colorvarient'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_varient',
            field=models.ManyToManyField(blank=True, to='store.sizevarient'),
        ),
    ]
