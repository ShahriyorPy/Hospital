# Generated by Django 4.2.5 on 2023-09-25 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asosiyAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qavat', models.PositiveIntegerField()),
                ('raqam', models.PositiveIntegerField()),
                ('sigim', models.PositiveIntegerField()),
                ('bosh_joy_soni', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Joylashtirish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelish_sana', models.DateField()),
                ('ketish_sana', models.DateField(blank=True, null=True)),
                ('qarovchi', models.BooleanField(default=False)),
                ('bemor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiyAPP.bemor')),
                ('xona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kasalxonaAPP.xona')),
            ],
        ),
    ]