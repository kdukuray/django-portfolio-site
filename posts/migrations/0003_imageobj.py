# Generated by Django 5.0.4 on 2024-05-20 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageObj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=30)),
                ('source', models.ImageField(upload_to='all_images')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
