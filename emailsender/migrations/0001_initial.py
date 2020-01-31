# Generated by Django 3.0.2 on 2020-01-31 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150, verbose_name='Текст')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('seconds', models.PositiveIntegerField(default=0, verbose_name='Секунды')),
            ],
        ),
    ]