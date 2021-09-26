# Generated by Django 3.2.5 on 2021-09-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('staff_count', models.IntegerField()),
            ],
            options={
                'db_table': 'colg',
            },
        ),
    ]