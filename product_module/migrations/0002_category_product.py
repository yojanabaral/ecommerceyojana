# Generated by Django 3.1.4 on 2021-03-05 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('registered_on', models.DateTimeField()),
                ('is_active', models.BooleanField()),
                ('color_code', models.CharField(max_length=20)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.brand')),
            ],
        ),
    ]