# Generated by Django 2.2 on 2019-05-02 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Автор'),
        ),
    ]