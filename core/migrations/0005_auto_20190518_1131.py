# Generated by Django 2.2.1 on 2019-05-18 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
    ]