# Generated by Django 3.0 on 2024-08-28 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]