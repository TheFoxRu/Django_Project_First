# Generated by Django 3.0.7 on 2020-06-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20200629_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(verbose_name='текст комментария'),
        ),
    ]
