# Generated by Django 4.2.5 on 2023-09-25 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bemor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('manzil', models.CharField(max_length=150)),
                ('tel', models.CharField(max_length=30)),
                ('joylashgan', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Yollanma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('qayerga', models.CharField(max_length=30)),
                ('narx', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tolov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField(auto_now_add=True)),
                ('tolandi', models.BooleanField(default=False)),
                ('summa', models.PositiveIntegerField()),
                ('tolangan_summa', models.JSONField(default=[])),
                ('haqdor', models.BooleanField(default=False)),
                ('turi', models.CharField(max_length=30)),
                ('bemor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiyAPP.bemor')),
            ],
        ),
    ]