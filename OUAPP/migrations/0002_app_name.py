# Generated by Django 2.2.4 on 2019-08-30 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OUAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='app_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_logo', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'app_name',
                'verbose_name_plural': 'app_names',
            },
        ),
    ]
