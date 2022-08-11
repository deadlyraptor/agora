# Generated by Django 4.0.5 on 2022-06-20 02:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import quantityfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_define_store_model'),
        ('products', '0001_define_product_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=quantityfield.fields.QuantityField(base_units='ounce', unit_choices=[
                                                     'ounce'], validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='brands', to='stores.store')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
