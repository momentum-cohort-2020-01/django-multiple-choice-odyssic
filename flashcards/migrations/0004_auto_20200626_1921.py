# Generated by Django 3.0.7 on 2020-06-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0003_auto_20200623_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='answer',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='card',
            name='question',
            field=models.CharField(max_length=80),
        ),
    ]