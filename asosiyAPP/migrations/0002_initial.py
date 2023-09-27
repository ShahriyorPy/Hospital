# Generated by Django 4.2.5 on 2023-09-25 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kasalxonaAPP', '0001_initial'),
        ('asosiyAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tolov',
            name='joylashtirish',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kasalxonaAPP.joylashtirish'),
        ),
        migrations.AddField(
            model_name='tolov',
            name='yollanma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asosiyAPP.yollanma'),
        ),
    ]
