# Generated by Django 4.1.5 on 2023-05-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='Описание')),
                ('office', models.CharField(blank=True, max_length=150, verbose_name='Офис')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='ContactPageForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('birth_day', models.DateField(auto_now_add=True, verbose_name='Дата рождения')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('phone', models.CharField(max_length=14, verbose_name='Телефон')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Изображение')),
                ('subject', models.CharField(max_length=100, verbose_name='Тема')),
                ('message', models.TextField(verbose_name='Текст сообщения')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
