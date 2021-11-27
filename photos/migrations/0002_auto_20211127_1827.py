# Generated by Django 3.2.9 on 2021-11-27 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='image',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.location'),
        ),
    ]
