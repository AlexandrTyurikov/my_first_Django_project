# Generated by Django 2.2 on 2019-04-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20190412_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publishing',
            options={'verbose_name': 'Издательство', 'verbose_name_plural': 'Издательства'},
        ),
        migrations.AlterField(
            model_name='products',
            name='publishing',
            field=models.ManyToManyField(to='products.Publishing'),
        ),
    ]
