# Generated by Django 3.0.7 on 2020-06-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200628_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_author',
            field=models.CharField(max_length=200, verbose_name='автор статьи'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_author',
            field=models.CharField(max_length=160, verbose_name='имя автора'),
        ),
    ]
