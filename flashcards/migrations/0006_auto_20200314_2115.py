# Generated by Django 3.0.4 on 2020-03-14 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0005_auto_20200313_0152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='cards',
            new_name='card',
        ),
    ]
