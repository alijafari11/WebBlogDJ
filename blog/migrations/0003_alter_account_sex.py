# Generated by Django 4.1.3 on 2023-10-21 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='sex',
            field=models.CharField(choices=[('man', 'Man'), ('woman', 'Woman')], default='men', max_length=5),
        ),
    ]
