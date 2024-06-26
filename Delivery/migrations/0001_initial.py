# Generated by Django 5.0.4 on 2024-05-22 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='home/')),
            ],
        ),
    ]
