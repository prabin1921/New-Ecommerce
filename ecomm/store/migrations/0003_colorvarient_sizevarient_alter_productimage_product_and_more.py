# Generated by Django 5.0.3 on 2024-03-13 07:12

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_slug_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorVarient',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('color', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SizeVarient',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('size', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='color_varient',
            field=models.ManyToManyField(to='store.colorvarient'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_varient',
            field=models.ManyToManyField(to='store.sizevarient'),
        ),
    ]
