# Generated by Django 4.2.3 on 2023-08-01 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_section_tag_articletag_articlesection_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.DeleteModel(
            name='ArticleTag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
