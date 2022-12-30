# Generated by Django 3.2 on 2022-12-30 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='check_unique',
            field=models.SlugField(help_text='Уникальность на урвне пользователя', null=True, verbose_name='уникальность'),
        ),
        migrations.AlterField(
            model_name='password',
            name='key',
            field=models.SlugField(help_text='Ключ доступа для вашего пароля', null=True, verbose_name='ключ'),
        ),
    ]
