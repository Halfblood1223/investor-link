# Generated by Django 3.1.7 on 2021-05-04 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_time', models.IntegerField()),
                ('monthly', models.IntegerField()),
                ('weekly', models.IntegerField()),
                ('daily', models.IntegerField()),
            ],
        ),
    ]