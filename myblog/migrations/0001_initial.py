# Generated by Django 4.2 on 2023-08-01 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=15)),
                ('slug', models.CharField(max_length=150)),
                ('post_images', models.ImageField(upload_to='postimg')),
            ],
        ),
    ]