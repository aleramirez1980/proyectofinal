# Generated by Django 4.2 on 2024-08-15 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vbc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acustica',
            name='email_contacto',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='amplificador',
            name='email_contacto',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='efecto',
            name='email_contacto',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='electrica',
            name='email_contacto',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]
