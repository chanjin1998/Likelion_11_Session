# Generated by Django 4.1.7 on 2023-03-26 17:05

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='email',
            field=models.EmailField(max_length=128, null=True),
        ),
    ]
