# Generated by Django 3.1.7 on 2021-05-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20210505_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='business_website',
            field=models.URLField(),
        ),
    ]
