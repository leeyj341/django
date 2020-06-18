# Generated by Django 2.1.15 on 2020-06-18 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('title_en', models.CharField(max_length=300)),
                ('audience', models.IntegerField()),
                ('open_date', models.DateTimeField()),
                ('genre', models.CharField(max_length=300)),
                ('watch_grade', models.CharField(max_length=300)),
                ('score', models.FloatField()),
                ('poster_url', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
