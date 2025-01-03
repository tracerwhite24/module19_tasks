# Generated by Django 4.2.17 on 2024-12-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='buyer',
            new_name='buyers',
        ),
        migrations.AlterField(
            model_name='buyer',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
