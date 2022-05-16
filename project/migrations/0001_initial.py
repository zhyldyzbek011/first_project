# Generated by Django 4.0.4 on 2022-04-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('lust_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('nationality', models.CharField(max_length=100)),
                ('height', models.IntegerField(blank=True)),
            ],
        ),
    ]