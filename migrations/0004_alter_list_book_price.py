# Generated by Django 3.2.7 on 2021-10-10 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookcatlog', '0003_list_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_book',
            name='price',
            field=models.IntegerField(),
        ),
    ]
