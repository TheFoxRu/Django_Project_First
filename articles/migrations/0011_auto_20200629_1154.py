# Generated by Django 3.0.7 on 2020-06-29 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20200629_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(max_length=255, verbose_name='текст комментария'),
        ),
    ]
