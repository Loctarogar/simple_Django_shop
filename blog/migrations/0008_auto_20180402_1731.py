# Generated by Django 2.0.1 on 2018-04-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180402_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='blog_tag', to='blog.Tag'),
        ),
    ]
