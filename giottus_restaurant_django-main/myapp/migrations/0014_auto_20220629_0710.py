# Generated by Django 2.2.12 on 2022-06-29 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20220629_0640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=150)),
                ('release_year', models.IntegerField()),
                ('director', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='myapp.Director')),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='hometown',
        ),
        migrations.RemoveField(
            model_name='person',
            name='living',
        ),
        migrations.RemoveField(
            model_name='person',
            name='visitation',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Province',
        ),
    ]
