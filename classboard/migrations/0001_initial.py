# Generated by Django 4.1.5 on 2023-05-13 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
        ('students', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_day', models.CharField(choices=[('1', 'Понедельник'), ('2', 'Вторник'), ('3', 'Среда'), ('4', 'Четверг'), ('5', 'Пятница'), ('6', 'Суббота'), ('7', 'Воскресенье')], default='1', max_length=6, verbose_name='День недели')),
                ('class_pair', models.CharField(choices=[('1', 'Первая пара'), ('2', 'Вторая пара'), ('3', 'Третья пара'), ('4', 'Четвертая пара'), ('5', 'Пятая пара'), ('6', 'Шестая пара'), ('7', 'Седьмая пара'), ('8', 'Восьмая пара')], default='1', max_length=6, verbose_name='Пара')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.group', verbose_name='Группа')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.subject', verbose_name='Занятие')),
                ('teacher', models.ManyToManyField(related_name='classboard_teacher', to='teachers.teacher', verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
                'ordering': ['subject_name'],
            },
        ),
    ]
