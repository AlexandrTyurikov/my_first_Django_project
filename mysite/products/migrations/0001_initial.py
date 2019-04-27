# Generated by Django 2.2 on 2019-04-23 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Автор(ы)')),
                ('description', models.TextField(verbose_name='Автобиография')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Жанр')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Publishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Издательство')),
                ('description', models.CharField(max_length=40, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательства',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Серия')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Серия',
                'verbose_name_plural': 'Серии',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Название книги')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Обложка')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('year', models.IntegerField(verbose_name='Год издания')),
                ('pages', models.IntegerField(verbose_name='Страниц')),
                ('binding', models.CharField(max_length=40, verbose_name='Переплет')),
                ('format', models.CharField(max_length=120, verbose_name='Формат')),
                ('isbn', models.CharField(max_length=40, verbose_name='ISBN')),
                ('weight', models.CharField(max_length=10, verbose_name='Вес')),
                ('age_limit', models.CharField(max_length=4, verbose_name='Возрастные ограничения')),
                ('sum', models.IntegerField(verbose_name='Количество книг в наличии')),
                ('available', models.BooleanField(default=True, verbose_name='Доступна для заказа')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Рейтинг')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
                ('author', models.ManyToManyField(related_name='products', to='products.Author', verbose_name='Автор(ы)')),
                ('genre', models.ManyToManyField(related_name='products', to='products.Genre', verbose_name='Жанр(ы)')),
                ('publishing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Publishing', verbose_name='Издательство')),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.Series', verbose_name='Серия')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['-name'],
            },
        ),
    ]
